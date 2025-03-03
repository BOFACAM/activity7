import requests
import passwords

user   = passwords.USERNAME
passwd = passwords.PASSWORD

url = f"http://localhost/basic-auth/{user}/{passwd}"
response = requests.get(url, auth=(user, passwd))

print(response.json())

