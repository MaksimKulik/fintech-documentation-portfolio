# Fintech Documentation Portfolio

A compact Material for MkDocs site containing selected product and API documentation samples for payment platforms.

Published site: <https://maksimkulik.github.io/fintech-documentation-portfolio/>

## First-time setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run locally

Activate the environment and start the development server:

```powershell
.\.venv\Scripts\Activate.ps1
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`.

You can also run MkDocs without activating the environment:

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

## Build

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

## Publish

Push changes to the `main` branch. GitHub Actions builds the site and publishes
it to the `gh-pages` branch automatically.
