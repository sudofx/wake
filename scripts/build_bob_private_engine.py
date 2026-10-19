#!/usr/bin/env python3
"""Build the pinned browser CPU engine without pthreads or shared WASM memory.

Writes build outputs only to the requested directory. Never opens an installation,
starts research, requests model output or publishes a website.
"""
import argparse
import hashlib
import io
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request


IMAGE = 'emscripten/emsdk@sha256:9bcd8da83ba146da138119daa6a8a5ced30d99610a3cc8755c183f5b929c4af5'
SOURCES = (
    ('ngxson/wllama', 'b68fd6427063266176bb0054befe9ff70b3258f1',
     '0ce93cafc1995a2f37365a4ef29da991fa39294ef82a439a5c0dbe8646e8979e', ''),
    ('ggml-org/llama.cpp', '46ca246de9bb1c35269722a6240d37d9dfd79cad',
     'c76f86403bca39af3bbbd21485309714d7610ece2d81324f828cc68c920a851d', 'llama.cpp'),
)
COMMAND = ('emcmake cmake -S . -B build-private -DWLLAMA_COMPAT=ON '
           '-DLLAMA_WASM_MEM64=OFF -DGGML_WEBGPU=OFF -DGGML_OPENMP=OFF '
           '-DLLAMA_CURL=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=OFF '
           '-DLLAMA_BUILD_SERVER=OFF -DBUILD_SHARED_LIBS=OFF && '
           'cmake --build build-private --target wllama -j4')


def prepare(source):
    for repository, revision, digest, child in SOURCES:
        url = f'https://codeload.github.com/{repository}/tar.gz/{revision}'
        with urllib.request.urlopen(url, timeout=120) as response:
            archive = response.read()
        if hashlib.sha256(archive).hexdigest() != digest:
            raise ValueError(f'Unexpected source archive bytes: {repository}')
        target = source / child
        target.mkdir(parents=True, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as bundle:
            for member in bundle:
                relative = Path(*Path(member.name).parts[1:])
                if relative == Path('.'):
                    continue
                member.name = str(relative)
                bundle.extract(member, target, filter='data')
    cmake = source / 'CMakeLists.txt'
    content = cmake.read_text()
    replacements = (
        ('set(CMAKE_THREAD_LIBS_INIT "-lpthread")', 'set(CMAKE_THREAD_LIBS_INIT "")'),
        ('set(CMAKE_USE_PTHREADS_INIT 1)', 'set(CMAKE_USE_PTHREADS_INIT 0)'),
        ('set(THREADS_PREFER_PTHREAD_FLAG ON)', 'set(THREADS_PREFER_PTHREAD_FLAG OFF)'),
    )
    for before, after in replacements:
        if content.count(before) != 1:
            raise ValueError('Pinned build configuration changed unexpectedly')
        content = content.replace(before, after)
    # A one-thread setting does not undo a binary compiled with -pthread.
    # Remove threading at compilation/linking and let WASM define private memory.
    content = '\n'.join(line for line in content.split('\n')
                        if line.strip() not in ('-pthread', '-sUSE_PTHREADS=1', '-sIMPORTED_MEMORY=1')
                        and '-sPTHREAD_POOL_SIZE=' not in line)
    cmake.write_text(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='wake-bob-private-build-') as directory:
        source = Path(directory)
        prepare(source)
        subprocess.run(['docker', 'run', '--rm', '--platform', 'linux/arm64',
                        '--cpus', '4', '--memory', '4g', '--network', 'none',
                        '-v', f'{source}:/source', '-w', '/source', IMAGE,
                        'bash', '-ec', COMMAND], check=True)
        for name in ('wllama.js', 'wllama.wasm'):
            target = output / name
            shutil.copyfile(source / 'build-private' / name, target)
            print(hashlib.sha256(target.read_bytes()).hexdigest(), target)


if __name__ == '__main__':
    main()
