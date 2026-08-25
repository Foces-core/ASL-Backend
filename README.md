# ASL backend

Flask backend for the ASL webapp. It currently provides a health check route and a placeholder question endpoint that returns an empty question payload for a given level, ready to be filled with real quiz data.

## API endpoints

| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | `/` | Returns a hello world message |
| GET | `/index` | Same handler as `/` |
| GET | `/question/<level>` | Returns the question for a level as JSON. Placeholder for now: all fields are `null` |

The question response has this shape:

```json
{
  "question": null,
  "options": null,
"optionCount": null,
  "xpOnSuccess": null
}
```

## Run locally

Requires Python 3.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS and Linux
pip install -r requirements.txt
flask --app app run --debug
```

The server listens on http://127.0.0.1:5000.

## Project structure

```
app/
├── __init__.py    # Creates the Flask app instance
└── routes.py      # All route definitions
requirements.txt   # Pinned dependencies (Flask 3.x)
```

## Security

This repository uses [gitleaks](https://github.com/gitleaks/gitleaks) for automatic secret scanning on every commit.

### Pre-commit hook

A pre-commit hook is configured to scan for secrets before each commit. This helps prevent accidentally committing sensitive information like:

- API keys
- Passwords
- Tokens
- Private keys

### Setup

To enable the pre-commit hook locally:

```bash
pip install pre-commit
pre-commit install
```

### Bypass (emergency only)

In case of emergency, you can bypass the hook:

```bash
git commit --no-verify -m "emergency commit"
```

> Only use `--no-verify` in emergency situations. Regular commits should always be scanned.
