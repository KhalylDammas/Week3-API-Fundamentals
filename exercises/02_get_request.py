import requests

URL = "https://api.restful-api.dev/objects"


# TODO 1:
# Send a GET request to URL and store the response.
response = requests.get("https://api.restful-api.dev/objects")


# TODO 2:
# Print the HTTP status code.
print(response.status_code)
# TODO 3:
# Convert the JSON response into a Python object.
data = response.json()


# TODO 4:
# Print the returned data.
print(data)

# TODO 5:
# Print how many objects were returned.
print()