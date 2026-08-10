# HTTP Server

A simple HTTP server built with Python's standard library using `HTTPServer` and `BaseHTTPRequestHandler`.

## Features

* Runs on `localhost:8080`
* `GET /status` endpoint
* JSON responses
* `404 Not Found` handling for unmapped routes
* `404 Not Found` handling for unsupported HTTP methods
* `uv` for environment and dependency management
* `pre-commit` for code-quality checks

## Requirements

* Python 3
* [uv](https://docs.astral.sh/uv/)
* Git

## Setup

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <project-directory>
```

Sync the project environment:

```bash
uv sync
```

Install the pre-commit hooks:

```bash
uv run pre-commit install
```

## Usage

Start the server:

```bash
python server.py
```

The server will be available at:

```text
http://localhost:8080
```

### Test the status endpoint

```bash
curl -i http://localhost:8080/status
```

Expected response:

```text
HTTP/1.0 200 OK
Content-Type: application/json
```

```json
{
  "status": "running",
  "code": 200,
  "message": "Server is operational"
}
```

### Test an invalid route

```bash
curl -i http://localhost:8080/other
```

Expected response:

```text
HTTP/1.0 404 Not Found
Content-Type: application/json
```

```json
{
  "error": "Endpoint not found"
}
```

### Test an unsupported HTTP method

```bash
curl -i -X POST http://localhost:8080/status
```

Expected response:

```text
HTTP/1.0 404 Not Found
Content-Type: application/json
```

```json
{
  "error": "Endpoint not found"
}
```

## Pre-commit

Pre-commit hooks are used to check the code before commits.

Run all hooks manually:

```bash
uv run pre-commit run --all-files
```

Once installed, the hooks will run automatically when committing changes.

## Stopping the Server

Press:

```text
Ctrl+C
```
