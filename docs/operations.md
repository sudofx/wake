# Operating the record

> **Current local-operations guide.** Use this for an independent local record, recovery and the legacy/alternate local publishing path. The GitHub-hosted deployment is documented in `cloud.md`.

**The GitHub-hosted research system uses [cloud operations](cloud.md).** The commands below operate an independent local record. Do not run a second live schedule against the cloud record’s API allowance.

## Everyday commands

Research topics are configured only in `research-topics.toml`; there is no hardcoded governance fallback. Topic-file changes are adopted as durable operator events when the record next loads the changed configuration. At the time of this documentation pass, the enabled configuration contains Consciousness, Psychology, Philosophy, Religion, Neurology and Endocrinology; that list is an operator-controlled experimental condition, not part of **WAKE✳︎**'s architecture.

Global options precede the command: `python3 -m wake --data data/another-record status`.

```sh
python3 -m wake status
python3 -m wake audit
python3 -m wake observe --source human:bench-test --text 'The measured output was 17; expected tolerance was 9–11.'
python3 -m wake focus 'Review contradictory measurements' --reason 'New bench result conflicts with the current belief.'
python3 -m wake cancel commitment-ID --reason 'The operator has withdrawn this task.'
python3 -m wake export --output site
python3 -m wake backup /absolute/path/to/new-backup.sqlite3
```

`data/wake.sqlite3` is the authoritative record. `site/` is generated and disposable. Keep private observations out of a journal you intend to publish. Exact model requests and replies are included in `events.jsonl` and the HTML audit view; the renderer does not silently redact scientific evidence. API keys and `.env` are never read into prompts or exports by **WAKE✳︎**.

Each export also creates human-readable companions for the two core machine exports: `events.md` and `events.html` present the complete event history, including exact model requests and replies, while `state.md` and `state.html` present the current durable state. These files are presentation layers only. `events.jsonl`, `state.json`, and the verified `head.txt` remain the audit sources of record.

## Scheduled wakes

First verify a single live `wake` and `export`. For a purely local installation, `python3 scripts/install_cron.py` can install the legacy managed local schedule. This explicitly edits your user crontab, preserving unrelated entries. `--print` shows the command first and `--remove` removes only **WAKE✳︎**’s entry. The installer records the absolute Python executable and project path, so cron does not need an activated environment.

The wrapper refreshes output even when a model rejects or fails. Every run keeps a SQLite backup under `data/backups/`; manage retention according to your storage budget. Backups are deliberately not silently deleted. Check `data/cron.log` and the journal's History view. The schedule uses the host cron timezone; the daily API limit and report dates always use Pacific time. The local installer uses its configured conservative cadence; actual provider limits and the per-model ceilings in `wake.toml` remain authoritative. A sleeping or disconnected host cannot run a wake; cron does not catch up missed cycles. macOS may require permission for cron to read a protected folder; keep the project in Developer rather than Downloads/Desktop.

To manually exercise exactly what cron will run: `python3 scripts/scheduled_wake.py`. This invokes the configured provider, so it can consume one live API call after free-tier opt-in.

## Read locally or publish through GitHub

For local desktop reading, open `site/index.html` or run `python3 -m wake serve`. Browser reading is HTML-first: `events.html` presents the complete audit trail, `state.html` presents durable state, and published notebooks/blog posts receive standalone reading pages. The Markdown and JSON/JSONL forms remain inspectable source artifacts; the verified machine record remains authoritative.

To read from another device on the same network:

```sh
python3 -m wake serve --host 0.0.0.0 --port 8000
```

Visit `http://YOUR-MACS-LAN-ADDRESS:8000` while the server is running. Anyone who can reach that port can read the exported report.

For the **current GitHub-hosted deployment**, do not configure a separate branch-based Pages publisher. The `WAKE✳︎ — research & journal` workflow exports the site and deploys it with GitHub Actions. In **Settings → Pages**, select **GitHub Actions** as the source. The durable runtime record lives separately on `wake-state`.

The repository still contains `scripts/publish.py` for an **independent local-only record** that an operator explicitly chooses to publish to a `journal-pages` branch. Treat that as a legacy/alternate publishing path, not part of the hosted **WAKE✳︎** architecture, and never point it at the same live record as the GitHub workflow.

The included `examples/journal/` is a shareable deterministic fixture report. Its simulated labels remain visible.

## Crash, corruption and recovery

```sh
python3 -m wake recover
python3 -m wake audit
python3 -m wake export
```

Recovery reconstructs a corrupt projection from valid event history and closes unfinished invocations. It does not refund an uncertain API attempt. Manual requests are only abandoned by explicit recovery, so a slow desktop reply is not silently lost.

If the event history itself is damaged, stop scheduled wakes. Preserve the damaged directory for investigation. Restore a separately retained SQLite backup into a **new** state directory as `wake.sqlite3`, then run `--data that-directory audit`, `recover` if needed, and `export`. Never recover by deleting inconvenient events. When resuming a backup from earlier today, use manual/fixture mode until the next Pacific day or account conservatively for calls made since the backup; the older ledger cannot know about later attempts.

To audit outside the database:

```sh
python3 -m wake audit --events site/events.jsonl --head /independently/retained/head.txt
```

The head must correspond to the export you are verifying. Store the export and its head together for reconstruction and retain another copy of the head separately for tamper/truncation detection.

## Updates and replacement

This is a new architecture, not a migration of older Bob identity/memory directories. Earlier experimental records remain in Git history and in the local pre-rebuild backup. Do not re-label them as verified v2 events. Private credentials can be retained in `.env`.

`scripts/package.py` creates a complete replacement ZIP using a source allowlist. Extracting the ZIP needs no existing files besides a usable Python installation. Runtime `data/`, backups and API keys are deliberately excluded; keep them separately when updating an existing v2 installation.
