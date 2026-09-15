# Week 3: API Fundamentals

## Assignment Overview

This assignment checks your understanding of networking and REST API fundamentals. You are **not** expected to build a complete application. Instead, you will answer short questions and practice making small Python programs that work with APIs.

The focus is on:

- Networking concepts
- URLs
- HTTP and HTTPS
- REST APIs
- GET and POST requests
- Python `requests`
- JSON
- Python dictionaries
- Git workflow

## Project Initialization

The supervisor has already provided this repository. Do not create a new repository. First, clone it and open the project folder:

```bash
git clone <repository-url>
cd week3-api-fundamentals
```

### Create a virtual environment

A virtual environment is an isolated Python environment for this project. Its dependencies are installed there instead of globally on your computer. The `.venv` folder should not be committed to Git.

Create and activate the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependency:

```bash
pip install -r requirements.txt
```

Check that `requests` was installed:

```bash
python -c "import requests; print(requests.__version__)"
```

Run an exercise like this:

```bash
python exercises/02_get_request.py
```

If your system uses `python3`, run:

```bash
python3 exercises/02_get_request.py
```

## Git Workflow

The assignment repository is already provided by your supervisor. Work in your own branch, complete the work gradually, and make commits as you finish sections.

```bash
git switch -c sara/week3
```

Example meaningful commits:

```text
Complete networking fundamentals answers
Complete URL exercises
Complete GET request exercises
Complete JSON dictionary exercises
Complete POST exercises
Complete DummyJSON independent exercises
```

Use Git throughout the assignment, not only when everything is finished. When you are ready, push your branch.

## Important Rules

- Write written and theoretical answers in `answers.md`.
- Write Python solutions only in the provided `.py` exercise files.
- Do not put Python solutions in `answers.md`.
- Run and test every Python file after completing it.
- Do not delete TODO comments before completing them.
- Do not replace an exercise with a completely different implementation unless necessary.
- Be ready to explain what your code does.

## Evaluation Focus

### Networking Concepts

Understanding of IP addresses, HTTP/HTTPS, ports, and URLs.

### API Concepts

Understanding of APIs, REST, HTTP methods, and the request/response flow.

### Python API Usage

Correct use of `requests.get()` and `requests.post()`.

### JSON and Dictionaries

Ability to convert response JSON, work with dictionaries and nested dictionaries/lists, and retrieve selected values.

### Problem Solving

Ability to complete the later exercises with less guidance.

### Git Usage

Git history should show gradual progress through multiple meaningful commits.
