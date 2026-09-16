"""Practice building URLs with strings, variables, and f-strings."""

# Exercise 1
base_url = "https://api.example.com"
resource = "users"
user_id = 15

url_component = [base_url,resource,str(user_id)]
url = "/".join(url_component)
# Build this URL:
# https://api.example.com/users/15


print(url)


# Exercise 2
base_url = "https://api.example.com"
resource = "products"
product_id = 42


# Here are going to create this URL using f-strings.
product_url = f"{base_url}/{resource}/{product_id}"

print(product_url)


# Exercise 3
base_url = "https://school.example.com"
resource = "students"
student_id = 8


student_url = base_url + "/" + resource + "/" + str(student_id)
print(student_url)


# Build this URL:
# https://school.example.com/students/8



