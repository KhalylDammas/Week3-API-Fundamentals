Create a complete starter GitHub repository for a Week 3 co-op training assignment.

The trainee is a diploma-level beginner who has already completed:

* Basic Python syntax
* Variables and data types
* Conditions
* Loops
* Functions
* Lists and dictionaries
* Simple classes
* File handling
* JSON
* Basic Git and GitHub usage

This week, the trainee was introduced to:

* IP addresses
* HTTP and HTTPS
* Ports
* URLs and URL components
* APIs
* REST APIs
* HTTP methods:

  * GET
  * POST
  * PUT
  * DELETE
* Python `requests`
* JSON API responses
* Working with JSON responses as Python dictionaries/lists

The purpose of this repository is **not to build a complete application**.

It is a knowledge-testing homework repository that combines:

1. Written conceptual questions
2. URL analysis questions
3. REST/HTTP reasoning questions
4. Guided Python TODO exercises
5. Independent Python API exercises
6. Git practice

The trainee should spend a significant amount of time actively writing, running, modifying, and debugging Python code in the IDE.

Do not overcomplicate the assignment.

---

# Repository Structure

Create this structure:

```text
week3-api-fundamentals/
│
├── README.md
├── answers.md
├── requirements.txt
├── .gitignore
│
└── exercises/
    ├── 01_url_building.py
    ├── 02_get_request.py
    ├── 03_get_single_object.py
    ├── 04_json_dictionaries.py
    ├── 05_post_request.py
    ├── 06_dummyjson_get.py
    └── 07_dummyjson_post.py
```

---

# README.md

The README should act as the main assignment instructions.

It should be clear, beginner-friendly, and structured.

Include the following sections.

## Assignment Overview

Explain that this assignment tests networking and REST API fundamentals.

Clarify that the trainee is not required to build an application.

The focus is understanding and practicing:

* Networking concepts
* URLs
* HTTP
* REST APIs
* GET and POST
* Python `requests`
* JSON
* Dictionaries
* Git workflow

---

# Project Initialization

This section is important.

The README must explain exactly how to initialize and run the project after cloning it.

Assume the trainee may be using Windows or Linux.

Start with cloning the repository:

```bash
git clone <repository-url>
cd week3-api-fundamentals
```

Then explain how to create a Python virtual environment.

For Windows:

```powershell
python -m venv .venv
```

Activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Also mention that Command Prompt activation would be:

```cmd
.venv\Scripts\activate.bat
```

For Linux/macOS:

```bash
python3 -m venv .venv
```

Activate it with:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

Explain briefly what a virtual environment is:

* It creates an isolated Python environment for the project.
* Project dependencies are installed there instead of globally.
* `.venv` should not be committed to Git.

Include how to verify `requests` is installed:

```bash
python -c "import requests; print(requests.__version__)"
```

Include how to run an exercise:

```bash
python exercises/02_get_request.py
```

On systems where Python is invoked using `python3`, mention:

```bash
python3 exercises/02_get_request.py
```

---

# Git Workflow

The trainee should not create a new repository.

The assignment repository is already provided by the supervisor.

The trainee should:

1. Clone the repository.
2. Create a working branch.
3. Complete the assignment gradually.
4. Commit completed sections as they work.
5. Push their branch.

Show an example:

```bash
git switch -c sara/week3
```

Show example meaningful commits:

```text
Complete networking fundamentals answers
Complete URL exercises
Complete GET request exercises
Complete JSON dictionary exercises
Complete POST exercises
Complete DummyJSON independent exercises
```

Explain that Git should be used throughout the assignment and not only at the end.

---

# Important Rules

Add a section clearly explaining:

* Written/theoretical answers go in `answers.md`.
* Python solutions must be written inside the provided `.py` exercise files.
* Do not put Python solutions inside `answers.md`.
* Run and test every Python file.
* Do not delete the TODO comments before completing them.
* Do not replace the exercise with a completely different implementation unless necessary.
* The trainee should be able to explain what their code does.

---

# answers.md

Create the theoretical questions in this file.

Each question should already have a placeholder such as:

```markdown
## Question 1

What is an IP address?

### Answer

Write your answer here.
```

Include approximately the following questions.

## Networking Questions

1. What is an IP address?
2. What purpose does an IP address serve?
3. What is HTTP?
4. What is HTTPS?
5. What is the difference between HTTP and HTTPS?
6. What is a port?
7. Why can one computer use multiple ports?
8. What are the commonly assigned ports for:

   * HTTP
   * HTTPS
   * SSH
9. What is a URL?
10. What purpose does a URL serve?
11. What is an API?
12. Give one example of why an application may use an API.
13. What is a REST API?

Use the correct terms:

* API = Application Programming Interface
* URL = Uniform Resource Locator

---

# URL Analysis Questions

Include this URL:

```text
https://learn.example.com:443/articles/security?from=2024&to=2026
```

Ask the trainee to identify:

* Scheme
* Hostname
* Port
* Path
* Query parameters

Then include:

```text
http://192.168.1.50:8080/users/5
```

Ask for:

* Scheme
* Host
* Port
* Path

Then include:

```text
https://api.example.com/products?category=laptop&limit=10
```

Ask for:

* Scheme
* Hostname
* Path
* Query parameters

---

# HTTP / REST Questions

Provide scenarios and ask which method should normally be used.

Methods:

```text
GET
POST
PUT
DELETE
```

Examples:

* Retrieve employee number 25
* Create a new request
* Retrieve all products
* Replace an existing product
* Delete an existing resource

Also ask:

* What is the main difference between GET and POST?
* What does an HTTP response represent?
* Why are JSON responses useful in Python applications?

---

# Request Flow Question

Include a final conceptual question using:

```python
response = requests.get(
    "https://api.restful-api.dev/objects/7"
)
```

Ask the trainee to explain what happens from the moment this line executes until the response is received.

Their explanation should involve:

* Python program
* URL
* HTTP
* GET
* API/server
* HTTP response
* JSON
* Python dictionary/list

Do not require low-level TCP/IP internals.

---

# Python Exercise Files

The Python exercises should gradually reduce the amount of guidance.

Early exercises should have detailed TODO comments.

Later exercises should mainly give requirements and allow the trainee to write the implementation independently.

The idea is:

```text
Heavy guidance
    ↓
Moderate guidance
    ↓
Few hints
    ↓
Independent implementation
```

---

# exercises/01_url_building.py

Create simple Python URL-building exercises.

Example:

```python
base_url = "https://api.example.com"
resource = "users"
user_id = 15

# TODO:
# Build:
# https://api.example.com/users/15

url = ""

print(url)
```

Add 2-3 similar exercises.

Use basic:

* Strings
* Variables
* f-strings

Do not introduce new libraries.

---

# exercises/02_get_request.py

Use:

```text
https://api.restful-api.dev/objects
```

Starter structure:

```python
import requests

URL = "https://api.restful-api.dev/objects"


# TODO 1:
# Send a GET request to URL and store the response.
response = None


# TODO 2:
# Print the HTTP status code.


# TODO 3:
# Convert the JSON response into a Python object.
data = None


# TODO 4:
# Print the returned data.


# TODO 5:
# Print how many objects were returned.
```

Do not provide the completed solution.

---

# exercises/03_get_single_object.py

Use:

```text
https://api.restful-api.dev/objects/7
```

Provide:

```python
import requests

OBJECT_ID = 7
```

TODOs should include:

* Build the URL using `OBJECT_ID`
* Send a GET request
* Convert the JSON response
* Print object ID
* Print object name
* Print HTTP status code

Use an f-string for URL construction.

---

# exercises/04_json_dictionaries.py

This file should primarily reinforce dictionaries and nested dictionaries.

Use:

```python
device = {
    "id": "7",
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9"
    }
}
```

TODOs:

* Print device name
* Print year
* Print CPU model
* Print price
* Update price
* Add:

```python
"available": True
```

* Print final dictionary

Add one additional simple nested dictionary exercise.

---

# exercises/05_post_request.py

Use:

```text
https://api.restful-api.dev/objects
```

Provide:

```python
import requests

URL = "https://api.restful-api.dev/objects"

new_object = {
    "name": "Training Laptop",
    "data": {
        "year": 2026,
        "department": "IT",
        "purpose": "Co-Op Training"
    }
}
```

TODOs:

* Send a POST request
* Use the `json=` argument
* Store the response
* Print status code
* Convert response JSON into a Python dictionary
* Print full response
* Print only returned ID
* Print returned object name

Do not provide the solution.

---

# exercises/06_dummyjson_get.py

This is an independent exercise.

Use:

```text
https://dummyjson.com/posts/1
```

Do not provide step-by-step starter code beyond:

```python
import requests
```

Provide requirements in the file docstring:

1. Send a GET request.
2. Convert the response JSON into a Python object.
3. Print the post ID.
4. Print the title.
5. Print the body.
6. Print the HTTP status code.
7. Print the number of likes inside the nested `reactions` object.

Mention that everything needed has already been practiced in the previous exercises.

---

# exercises/07_dummyjson_post.py

This should be the most independent exercise.

Use:

```text
https://dummyjson.com/posts/add
```

Provide only:

```python
import requests

new_post = {
    "title": "Learning REST APIs",
    "body": "This post was created using Python requests.",
    "userId": 1
}
```

Requirements:

1. Send `new_post` using POST.
2. Send it as JSON.
3. Convert the response JSON into a Python object.
4. Print the complete returned object.
5. Print the returned ID.
6. Print the title.
7. Print the HTTP status code.

Add a comment explaining:

DummyJSON simulates POST creation. The resource is returned as if it were created, but it is not permanently stored.

---

# requirements.txt

Create:

```text
requests
```

Do not add unnecessary packages.

---

# .gitignore

Create an appropriate beginner-friendly Python `.gitignore`.

At minimum include:

```text
.venv/
__pycache__/
*.pyc
```

Also include common IDE files where reasonable, but keep it simple.

Do not ignore the actual exercise files.

---

# Coding Style

Keep all Python code intentionally simple.

The trainee is a beginner.

Use only concepts already taught.

Avoid:

* Async code
* Classes unless necessary
* Decorators
* Type annotations unless extremely simple
* Custom exception classes
* Context managers beyond concepts already learned
* Databases
* FastAPI
* Flask
* Authentication
* API keys
* Advanced HTTP headers
* Sessions
* Environment variables
* Packaging
* Complex project architectures

The purpose is not to demonstrate advanced Python.

The purpose is to reinforce beginner Python while introducing API interaction.

---

# Evaluation Focus

Include an evaluation section in README.md.

Use these categories:

## Networking Concepts

Understanding of:

* IPs
* HTTP/S
* Ports
* URLs

## API Concepts

Understanding of:

* APIs
* REST
* HTTP methods
* Request/response flow

## Python API Usage

Correct use of:

```python
requests.get()
```

and:

```python
requests.post()
```

## JSON and Dictionaries

Ability to:

* Convert response JSON
* Work with dictionaries
* Work with nested dictionaries/lists
* Retrieve selected values

## Problem Solving

Ability to complete the later exercises with less guidance.

## Git Usage

Git should show gradual progress through multiple meaningful commits.

---

# General Quality Requirements

Before finishing:

1. Verify all Markdown formatting.
2. Verify all Python files are syntactically valid starter files.
3. Do not accidentally include completed TODO solutions.
4. Verify all referenced API URLs are correct.
5. Make sure `requirements.txt` contains only required dependencies.
6. Make sure `.venv/` is ignored.
7. Make the README usable by someone cloning the repository for the first time.
8. Keep the assignment appropriate for a diploma trainee in their third week.
9. Do not make the wording overly academic or corporate.
10. Prefer simple explanations and direct instructions.

The finished repository should feel like a real coding exercise repository that the trainee can clone, open in VS Code or another IDE, initialize, complete, run, commit, and push.
