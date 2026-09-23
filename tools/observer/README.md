# WAKE Observer

Local, read-only analysis for WAKE's `wake-state` branch. It can fetch a public GitHub record directly or
read an existing local WAKE checkout, explains the latest outcome, highlights repeat failures and attention
signals, and can ask Gemini for an explicitly non-authoritative analyst opinion.

```sh
cd wake-observer
cp .env.example .env
# edit .env: add GEMINI_API_KEY and optionally WAKE_OBSERVER_REPOSITORY
python3 app.py
# open http://127.0.0.1:8765
```

On first run, select either a local checkout or a public GitHub `owner/repository` (for example,
`sudofx/wake`) and its state branch (`wake-state`). The app remembers only that source selection in
`observer-config.json`. `GEMINI_API_KEY` is optional and is read only from the local `.env` file.

The app sends only its generated report to Gemini. It never writes to WAKE, starts a wake, or changes state.
