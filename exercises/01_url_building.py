"""Practice building URLs with strings, variables, and f-strings."""

# Exercise 1
base_url = "https://api.example.com"
resource = "users"
user_id = 15

# TODO:
# Build this URL:
# https://api.example.com/users/15
url_component = [base_url,resource,str(user_id)]
url = "https://api.example.com".join(url_component)

print(url)


# Exercise 2
base_url = "https://api.example.com"
resource = "products"
product_id = 42

# TODO:
# Build this URL:
# https://api.example.com/products/42
product_url = "https://api.example.com/products/42"
url_component =[base_url,resource,str(user_id)]
url = product_url.upper()

print(product_url)


# Exercise 3
base_url = "https://school.example.com"
resource = "students"
student_id = 8

# TODO:
# Build this URL:
# https://school.example.com/students/8
student_url = " https://school.example.com/students/8"
url_component = [base_url,resource,str(user_id)]
url =  student_url.lower()

print(student_url)

