"""Practice reading and changing dictionaries and nested dictionaries."""

device = {
    "id": "7",
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9"
    }
}

# TODO 1: Print the device name.
print(device["name"])

# TODO 2: Print the year.
print(device["data"]["year"])

# TODO 3: Print the CPU model.
print(device["data"]["CPU model"])

# TODO 4: Print the price.
print(device["data"]["price"])

# TODO 5: Update the price to a new value of your choice.
device ["data"]["price"] = 3500
# TODO 6: Add "available": True to the device dictionary.
device ["avalible"] = True
# TODO 7: Print the final dictionary.
print(device)

# Additional nested dictionary exercise
student = {
    "name": "Sara",
    "course": {
        "title": "API Fundamentals",
        "week": 3
    }
}

# TODO 8: Print the student's name.
print(student["name"])
# TODO 9: Print the course title.
print(student["course"]["title"])
# TODO 10: Change the course week to 4, then print the final student dictionary.
student["course"]["week"] = 4
print(student)