import requests

new_post = {
    "title": "Learning REST APIs",
    "body": "This post was created using Python requests.",
    "userId": 1
}

# DummyJSON simulates POST creation. The resource is returned as if it were
# created, but it is not permanently stored.

# Requirements:
# 1. Send new_post to https://dummyjson.com/posts/add using POST.
# 2. Send it as JSON.
# 3. Convert the response JSON into a Python object.
# 4. Print the complete returned object.
# 5. Print the returned ID.
# 6. Print the title.
# 7. Print the HTTP status code.
response = requests.post("https://dummyjson.com/posts/add", json=new_post)

data = response.json()

print(data)
print(data["id"])
print(data["title"])
print(response.status_code)