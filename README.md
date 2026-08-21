# DevOps-Week-02

A sample project to demonstrate Git and GitHub workflow for DevOps practices.

## Project Structure

- `app.py` – Main application entry point.
- `config.yaml` – Application configuration.
- `requirements.txt` – Python dependencies.
- `Dockerfile` – Container definition.
- `.gitignore` – Git ignore rules.

## Features

- Basic Python application.
- Logging integration.
- Production-ready configuration.
- Dockerized deployment.

## Branching Strategy

- `main` – Stable, production-ready code.
- `feature/logging` – Added logging to the application.
- `feature/config-update` – Updated configuration and app behavior for production.

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

## Docker

```bash
docker build -t devops-week-02 .
docker run devops-week-02
```
