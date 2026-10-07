FROM python:3.13-slim-bookworm AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 HOME=/home/wake
RUN apt-get update && apt-get install -y --no-install-recommends openssl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY wake ./wake
COPY wake.toml research-topics.toml ./
RUN python -m pip install . && groupadd --gid 10001 wake && useradd --uid 10001 --gid wake --create-home --shell /bin/bash wake && mkdir /data && chown wake:wake /data
USER 10001:10001
VOLUME ["/data"]
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/runtime.json', timeout=3).read()"
ENTRYPOINT ["python", "-m", "wake.standalone"]

# Optional editor tools; the default standalone image stays minimal.
FROM runtime AS vscode
USER root
RUN apt-get update && apt-get install -y --no-install-recommends git openssh-client && rm -rf /var/lib/apt/lists/* && git config --system --add safe.directory /workspace
USER 10001:10001

FROM runtime AS standalone
