# Week 3 Written Answers

Write your answers below each question in your own words.

## General Knowledge

### Question 1

What is an IP address?

`TODO Answer`

Write your answer here.
An IP address is a number that identifies a device on a network

### Question 2

What purpose does an IP address serve?

`TODO Answer`

Write your answer here.

It helps devices communicate with each other.

### Question 3

What is HTTP?

`TODO Answer`

Write your answer here.

HTTP is used to send and receive data over the internet

### Question 4

What is HTTPS?

`TODO Answer`

Write your answer here.

HTTPS is a secure version of HTTP.

### Question 5

What is the difference between HTTP and HTTPS?

`TODO Answer`

Write your answer here.

HTTPS is more secure than HTTP

### Question 6

What is a port?

`TODO Answer`

Write your answer here.

A port is used to connect to a service on a network

### Question 7

Why can one computer use multiple ports?

`TODO Answer`

Write your answer here.

A computer can use multiple ports for different services

### Question 8

What are the commonly assigned ports for HTTP, HTTPS, and SSH?

`TODO Answer`

Write your answer here.

HTTP uses port 80, HTTPS uses port 443, and SSH uses port 22

### Question 9

What is a URL (Uniform Resource Locator)?

`TODO Answer`

Write your answer here.

A URL is the address of a website or resource on the internet

### Question 10

What purpose does a URL serve?

`TODO Answer`

Write your answer here.

A URL tells us where a website or resource is located

### Question 11

What is an API (Application Programming Interface)?

`TODO Answer`

Write your answer here.

An API allows applications to communicate with each other

### Question 12

Give one example of why an application may use an API.

`TODO Answer`

Write your answer here.

An app can use an API to get information from another service

### Question 13

What is a REST API?

`TODO Answer`

Write your answer here.

A REST API is an API that uses HTTP methods to work with data

## URL Analysis

### Question 14

For this URL:

```text
https://learn.example.com:443/articles/security?from=2024&to=2026
```

Identify the scheme, hostname, port, path, and query parameters.

`TODO Answer`

Write your answer here.

Scheme: https
Hostname: learn.example.com
Port: 443
Path: /articles/security
Query parameters: from=2024, to=2026

### Question 15

For this URL:

```text
http://192.168.1.50:8080/users/5
```

Identify the scheme, host, port, and path.

`TODO Answer`

Write your answer here.

Scheme: http
Host: 192.168.1.50
Port: 8080
Path: /users/5

### Question 16

For this URL:

```text
https://api.example.com/products?category=laptop&limit=10
```

Identify the scheme, hostname, path, and query parameters.

`TODO Answer`

Write your answer here.

Scheme: https
Hostname: api.example.com
Path: /products
Query parameters: category=laptop, limit=10

## HTTP and REST

### Question 17

Which HTTP method should normally be used for each scenario? Choose from `GET`, `POST`, `PUT`, and `DELETE`.

- Retrieve employee number 25
- Create a new request
- Retrieve all products
- Replace an existing product
- Delete an existing resource

`TODO Answer`

Write your answer here.
1: GET
2: POST
3:GET
4:PUT
5:DELETE

### Question 18

What is the main difference between GET and POST?

`TODO Answer`

Write your answer here.

GET is used to get data , POST is used to send data

### Question 19

What does an HTTP response represent?

`TODO Answer`

Write your answer here.

An HTTP response is the data sent back by the server after a request

### Question 20

Why are JSON responses useful in Python applications?

`TODO Answer`

Write your answer here.

JSON can be easily converted to dictionaries and lists in Python

## Request Flow

### Question 21

Explain what happens from the moment this line executes until the response is received:

```python
response = requests.get(
    "https://api.restful-api.dev/objects/7"
)
```

Include the Python program, URL, HTTP, GET, API/server, HTTP response, JSON, and Python dictionary/list in your explanation. You do not need to explain low-level TCP/IP internals.

`TODO Answer`

Write your answer here.

The Python program sends a GET request to the API/server using HTTP The server sends an HTTP response with JSON data which Python converts into a dictionary or list
