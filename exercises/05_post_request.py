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

# TODO 1:
# Send a POST request to URL. Use the json= argument to send new_object.
response = requests.post(URL, json=new_object)

# TODO 2: Print the HTTP status code.
print(response.status_code)
# TODO 3: Convert the response JSON into a Python dictionary.
data = response.json()

# TODO 4: Print the full response dictionary.
print(data)
# TODO 5: Print only the returned ID.
print(data["id"])
# TODO 6: Print the returned object name.
print(data["name"])