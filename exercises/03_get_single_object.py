import requests

OBJECT_ID = 7

# TODO 1:
# Build the URL below using OBJECT_ID and an f-string.
# The final URL should be https://api.restful-api.dev/objects/7
URL = f" https://api.restful-api.dev/objects/{OBJECT_ID}"

# TODO 2:
# Send a GET request and store the response.
response = requests.get(URL)

# TODO 3:
# Convert the response JSON into a Python dictionary.
data = response.json()

# TODO 4:
# Print the object ID.
print(data["id"])

# TODO 5:
# Print the object name.
print(data["name"])

# TODO 6:
# Print the HTTP status code.
print(response.status_code)
