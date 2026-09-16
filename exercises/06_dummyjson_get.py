"""
Independent exercise: everything needed has already been practiced earlier.

Use https://dummyjson.com/posts/1 and complete these requirements:
1. Send a GET request.
2. Convert the response JSON into a Python object.
3. Print the post ID.
4. Print the title.
5. Print the body.
6. Print the HTTP status code.
7. Print the number of likes inside the nested reactions object.
"""

import requests
response = requests.get(" https://dummyjson.com/posts/1")

data =response.json()

print(data["id"])

print(data["title"])

print(data["body"])

print(response.status_code)

print(data["reactions"]["likes"])
