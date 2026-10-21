# Set up WAKE✳︎

Choose one path. Each installation has its own records. A website copy is not a
research installation, and creating a new environment does not copy existing research.

| What you want | Follow these steps |
| --- | --- |
| WAKE on your computer | [Local Docker](#1-local-docker-installation) |
| A public website on GitHub | [GitHub Pages](#2-github-pages-website) |
| Edit WAKE in desktop VS Code | [Local development](#3-develop-in-vs-code) |
| Run and edit WAKE in your browser | [Codespaces](#4-run-and-develop-in-codespaces) |

## 1. Local Docker installation

This creates one container named `wake`. Inside it are twelve research workers and
one website. Research starts stopped. You can inspect WAKE without a model key.

### Step 1 — Start Docker

Install and start Docker Desktop on macOS or Windows, or Docker Engine on Linux.
On Windows, run the commands below in a WSL shell with Docker integration enabled.
You need a POSIX shell, `curl`, `tar`, internet access, and permission to use Docker.
Check that Docker is ready:

```sh
docker info
```

If this fails, start Docker or fix your shell's Docker access before continuing.

### Step 2 — Install and start WAKE

Run this from any directory:

```sh
curl -fsSL https://raw.githubusercontent.com/sudofx/wake/refs/heads/master/container_setup.sh | sh
```

The script downloads source to `$HOME/.local/share/wake`, builds the image, and
starts the container. On later runs, it finds the managed container and its source
folder. It does not replace an existing checkout or change running research controls.
If an unrelated container already uses the name `wake`, it stops with an explanation.

To inspect the script before running it, use:

```sh
curl -fsSL https://raw.githubusercontent.com/sudofx/wake/refs/heads/master/container_setup.sh -o container_setup.sh
sh container_setup.sh
```

To use an existing checkout or a different port, pass settings to the shell that
runs the installer:

```sh
curl -fsSL https://raw.githubusercontent.com/sudofx/wake/refs/heads/master/container_setup.sh |
  WAKE_INSTALL_DIR="$HOME/Developer/wake" WAKE_PORT=8090 sh
```

The existing checkout must contain `scripts/wake_installation`. An archive install
has source files but no Git history; use a Git clone for development and source pushes.

### Step 3 — Open the website

Open **http://localhost:8080/console.html**. Use your selected port if different.
The main site is **http://localhost:8080/**. Initialization can take a few minutes.
The installer prints the actual published port and reports when the server responds.

### Step 4 — Inspect the installation

From any shell with Docker access:

```sh
docker exec wake wake-research status
```

To enter its shell:

```sh
docker exec -it wake bash
```

Inside the container, `wake-research status` reports the same installation.
The node selector is available on Console pages.

### Step 5 — Configure research, if wanted

On your computer, open the installation's source folder. For the default install:

```sh
cd "$HOME/.local/share/wake"
test -f .env || cp .env.example .env
```

Edit `.env` and set `GEMINI_API_KEY` to your own key. Edit `research-topics.toml`
to choose topics. Keep credentials in `.env`; do not commit them. Confirm provider
model names, limits and billing settings before enabling live calls.

Recreate the container to load changed environment settings:

```sh
sh container_setup.sh recreate
```

The downloaded source includes this script. From another directory, use the full
path or run the remote command again with `sh -s -- recreate`.
Recreation builds first, checks disposable copies of existing records against the
new code, drains active research, and then replaces the container. The records stay
in `data/installation`. The previous container remains stopped under a printed
backup name. Research in the replacement starts stopped.

If the record check fails, the launcher leaves the original container running.
Keep its working source version; an unsupported record needs a separate, reviewed
migration. Recreating a container is not a record reset.

### Step 6 — Start research explicitly

```sh
docker exec wake wake-research start
```

Check progress later with `docker exec wake wake-research status`. A running state
means research is enabled; accepted progress may wait for sources or provider quota.
To stop research while keeping the website available:

```sh
docker exec wake wake-research stop
```

### Step 7 — Stop, restart, or recreate later

Save the installer locally to use these commands from any directory:

```sh
sh "$HOME/.local/share/wake/container_setup.sh" status
sh "$HOME/.local/share/wake/container_setup.sh" stop
sh "$HOME/.local/share/wake/container_setup.sh" start
sh "$HOME/.local/share/wake/container_setup.sh" recreate
```

`start` keeps a running container as it is. `recreate` builds from the source already
on disk; it does not download updates or overwrite edits. In a Git clone, review
and update source explicitly before recreating. Keep `data/installation` and its
backups. The installer never deletes data volumes or issues the destructive `RESET`.
If replacement fails after the old container is stopped, both its printed backup
name and the record directory remain available for inspection.

For all controls, manual record archives and LAN access, see
[local operation](standalone.md#control-research-from-the-shell).

## 2. GitHub Pages website

GitHub Pages serves a public, read-only copy of an installation's website. It does
not run Python or research. You need a GitHub account, your own public repository,
Git, GitHub CLI (`gh`), Python 3.11 or later, and the local installation above.

### Step 1 — Create your repository

On GitHub, fork `sudofx/wake` into your account. Keep your repository public for
GitHub's free public-repository Pages option. Record its URL, such as
`https://github.com/YOUR-NAME/wake`.

### Step 2 — Sign in from your computer

```sh
gh auth login
```

Use your own account with write access to that repository. Never put a GitHub token
in the website or source files.

### Step 3 — Prepare the publisher

In your local WAKE source folder:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

Edit `.env` and add your destination, replacing `YOUR-NAME`:

```sh
WAKE_PUBLISH_REPOSITORY=https://github.com/YOUR-NAME/wake
WAKE_PUBLISH_BRANCH=wake-public
```

Keep `master` for source. `wake-public` is only the generated website.

### Step 4 — Upload the website

Make sure the local container is running and has completed its first exports.
Wait for any running Actions jobs in the destination repository to finish, then run:

```sh
./scripts/wake_publish
```

This captures completed exports and uploads them. It does not start, stop or reset
research. It requires the publisher dependencies above in the active shell.

### Step 5 — Turn on Pages

In your repository, open **Settings → Pages**. Under **Build and deployment**:

1. Choose **Deploy from a branch**.
2. Select **wake-public**.
3. Select **/ (root)**.
4. Click **Save**.

These are GitHub's [branch publishing settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

### Step 6 — Check the public website

Wait for the Pages build to finish in **Actions**. Open the website URL shown in
**Settings → Pages**, normally `https://YOUR-NAME.github.io/wake/`.
Check the Console's snapshot date against your upload. Successful upload and
successful Pages deployment are separate checks.

### Step 7 — Keep it current

From the same source folder with `.venv` active:

```sh
./scripts/wake_publish --watch
```

Keep this publisher process and the local container available. It delivers new
completed snapshots; it does not make research run on GitHub. Stop automatic
publishing with `docker exec wake wake-research mirror-disable`.

For laptop-independent research, GitHub Actions needs a separate, explicitly
initialized encrypted installation. The Pages steps above do not configure it.
See [hosted research](cloud.md#run-research-on-github-without-a-laptop) for its
credentials, verified checkpoint requirements, controls and recovery contract.

## 3. Develop in VS Code

### Step 1 — Clone the source

Install Git, VS Code and its **Dev Containers** extension. Clone your fork to a
new directory, or use the existing Git checkout you intend to develop:

```sh
git clone https://github.com/YOUR-NAME/wake.git
cd wake
```

### Step 2 — Start the local development container

```sh
sh container_setup.sh
```

If another managed `wake` container uses a different checkout, the launcher stops.
Use that checkout or stop and explicitly plan a separate installation; changing
folders does not authorize replacing someone else's records.

### Step 3 — Attach VS Code

Open the command palette and choose **Dev Containers: Attach to Running Container…**,
then choose **wake**. In the attached window, open **/workspace**.
The terminal uses the installation's existing shell and `wake-research` commands.
On Linux, the runtime user is UID 10001; ensure the mounted checkout is writable
by that user before editing inside the container. Host-side editing remains available.

### Step 4 — Change and check code

Edit source under `/workspace`. Run the offline tests in the container terminal:

```sh
python -m unittest discover -s tests -v
```

Workers use a fixed source snapshot. To adopt changed code without starting
research, run `sh scripts/wake_installation restart` from the host source folder.
It checks record compatibility first. Inspect again, then explicitly start research
if wanted. `wake-research restart` is different: it also enables research.

### Step 5 — Save and publish source separately

Review `git diff`, run the relevant checks, then commit and push to your fork.
Source pushes do not upload the website, copy records, or update a running local
container. Use the Pages steps when you want to publish a new website snapshot.

## 4. Run and develop in Codespaces

A Codespace is a separate computer and a separate WAKE installation. You do not
need Docker on your laptop for this path. Codespaces usage has account quotas and
possible charges; check your GitHub spending settings before creating one.

### Step 1 — Create a Codespace

Open your fork on GitHub. Choose **Code → Codespaces → Create codespace on master**.
Wait for the committed Dev Container to build. It uses the same WAKE installation
controller and starts it stopped on port 8080.
GitHub documents [creating a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository).

### Step 2 — Open the Console

In VS Code's **Ports** panel, find port **8080** and open its browser link. Keep its
visibility **Private**. Use `/console.html` for Console or `/` for the main site.
If the service is not running, use the terminal:

```sh
python scripts/installation_preview.py start
```

See GitHub's [forwarded port guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).

### Step 3 — Inspect before research

```sh
wake-research status
```

The records are in `data/installation` inside this workspace. They are independent
of your laptop and hosted installation. Opening the Codespace does not import
research or start provider calls.

### Step 4 — Add a provider key only if needed

In GitHub account **Settings → Codespaces → Secrets**, add `GEMINI_API_KEY` and give
this repository access. Stop and restart the Codespace so the environment receives
it. Edit `research-topics.toml` in the workspace. Then explicitly enable research:

```sh
wake-research start
```

Codespaces secrets are separate from repository Actions secrets. See
[Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).

### Step 5 — Develop and test

Edit the mounted checkout and run:

```sh
python -m unittest discover -s tests -v
```

To reload changed controller and worker code while leaving research stopped:

```sh
python scripts/installation_preview.py stop
python scripts/installation_preview.py start
wake-research status
```

Stop waits for controller shutdown before the next start, so two controllers never
write the same records. Start explicitly again if you want research to resume.

### Step 6 — Finish safely

Commit and push source changes you want to keep. Export any research records you
need with `wake-research export --name codespace-records.zip` and download the
archive from `data/installation/backups` before deleting the Codespace. Git does
not save ignored research databases. Stop the Codespace from its GitHub menu when
finished. An idle or stopped Codespace cannot provide continuous hosted research.

## If something goes wrong

| What you see | What to do |
| --- | --- |
| Docker cannot connect | Start Docker and check `docker info`. |
| Port 8080 is already in use | Choose `WAKE_PORT=8090` when creating the container. |
| A different container is named `wake` | Inspect it; the installer will not replace it. |
| An upgrade check fails | Keep the current working source and container; inspect a copy of its records before planning migration. |
| The server does not become ready | Read `docker logs wake`; confirm topics exist and data is writable. |
| Research is stopped | Inspect first, then use `wake-research start` if intended. |
| Research is waiting for quota | Wait for the reported retry time; restarting does not create more quota. |
| Pages shows an older snapshot | Check upload success and the separate Pages build. |
