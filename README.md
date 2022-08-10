# author_today.py
Web-API for [author_today](https://author.today) website for reading books

![](https://i.ibb.co/bPczC1g/1636977124081.jpg)

## Example
```py3
# Simple Login
import author_today
client = author_today.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
```
