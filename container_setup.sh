#!/bin/sh
# Bootstrap the maintained launcher. Existing source and records are never replaced.
set -eu

main() {
    action=${1:-start}
    case "$action" in
        start|build|recreate|stop|restart|status|shell) ;;
        -h|--help|help)
            printf '%s\n' 'Usage: sh container_setup.sh [start|build|recreate|stop|restart|status|shell]' \
                'Default: start an existing managed container, or download, build and create one.' \
                'WAKE_INSTALL_DIR selects the checkout (default: $HOME/.local/share/wake).' \
                'WAKE_PORT selects the host port for a new container (default: 8080).'
            return ;;
        *) printf 'Unknown action: %s\n' "$action" >&2; return 2 ;;
    esac
    command -v docker >/dev/null 2>&1 || { echo 'Install Docker, then run this command again.' >&2; return 1; }
    docker info >/dev/null 2>&1 || { echo 'Start Docker and check that this shell can use it.' >&2; return 1; }
    # An existing container identifies its own checkout, even from an unrelated shell.
    if docker container inspect wake >/dev/null 2>&1; then
        owner=$(docker inspect --format '{{index .Config.Labels "com.sudofx.wake.installation"}}' wake)
        [ "$owner" = true ] || { echo 'A different container is named wake; it was not changed.' >&2; return 1; }
        installed=$(docker inspect --format '{{range .Mounts}}{{if eq .Destination "/workspace"}}{{.Source}}{{end}}{{end}}' wake)
        [ -n "$installed" ] || { echo 'The managed container has no source mount; inspect it before continuing.' >&2; return 1; }
        if [ -n "${WAKE_INSTALL_DIR:-}" ] && [ "$WAKE_INSTALL_DIR" != "$installed" ]; then
            echo 'WAKE_INSTALL_DIR differs from the existing container checkout; it was not changed.' >&2
            return 1
        fi
        install_dir=$installed
        if [ -z "${WAKE_PORT:-}" ]; then
            WAKE_PORT=$(docker inspect --format '{{(index (index .HostConfig.PortBindings "8080/tcp") 0).HostPort}}' wake)
        fi
    else
        install_dir=${WAKE_INSTALL_DIR:-${HOME:?Set HOME or WAKE_INSTALL_DIR}/.local/share/wake}
    fi
    case "$install_dir" in /*) ;; *) install_dir="$(pwd)/$install_dir" ;; esac
    if [ ! -f "$install_dir/scripts/wake_installation" ]; then
        case "$action" in start|build) ;; *) echo 'No installation found. Run the installer without an action first.' >&2; return 1 ;; esac
        [ ! -e "$install_dir" ] || { echo 'The target directory already exists without a WAKE launcher; choose another WAKE_INSTALL_DIR.' >&2; return 1; }
        command -v curl >/dev/null 2>&1 || { echo 'Install curl, then run this command again.' >&2; return 1; }
        command -v tar >/dev/null 2>&1 || { echo 'Install tar, then run this command again.' >&2; return 1; }
        parent=$(dirname "$install_dir")
        mkdir -p "$parent"
        staging=$(mktemp -d "$parent/.wake-download.XXXXXX")
        trap 'rm -rf "$staging"' EXIT HUP INT TERM
        echo 'Downloading WAKE source…'
        curl -fL --retry 3 'https://github.com/sudofx/wake/archive/refs/heads/master.tar.gz' -o "$staging/source.tar.gz"
        mkdir "$staging/source"
        tar -xzf "$staging/source.tar.gz" -C "$staging/source" --strip-components=1
        [ -f "$staging/source/scripts/wake_installation" ] || { echo 'The download did not contain the WAKE launcher.' >&2; return 1; }
        mv "$staging/source" "$install_dir"
        rm -rf "$staging"
        trap - EXIT HUP INT TERM
    fi
    export WAKE_PORT=${WAKE_PORT:-8080}
    exec sh "$install_dir/scripts/wake_installation" "$action"
}

# Keep execution last so an incomplete piped download cannot run a partial installer.
main "$@"
