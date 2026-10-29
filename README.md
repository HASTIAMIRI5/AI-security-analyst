# AI Security Analyst

A lightweight web app for scanning pasted code snippets for common security weaknesses and ranking the overall risk level.

## Features
- Paste code or a security-relevant snippet into the interface
- Detect common issues such as:
  - dangerous code execution (`eval`, `exec`)
  - SQL injection patterns
  - hardcoded secrets and tokens
  - insecure session/auth patterns
  - unsafe serialization and weak cryptography
- Display a risk score and prioritized recommendations
- Run locally in a single Python app

## Tech Stack
- Python
- Flask
- HTML/CSS/JavaScript

## Quick Start

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:
   ```bash
   python app.py
   ```

4. Open the app in your browser at:
   ```text
   http://127.0.0.1:5000/
   ```

## Example Security Checks

The analyzer looks for common risky patterns, including:
- `eval(` and `exec(`
- direct string concatenation in SQL statements
- `password = "..."` or API keys embedded in source files
- `pickle.loads`, `yaml.load`, and similar unsafe deserialization usage
- weak cryptographic algorithms such as MD5 or SHA1

This app is intentionally rule-based and fast, making it suitable for demos and local analysis workflows.
