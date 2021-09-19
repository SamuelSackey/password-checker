import re

pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}[0-9]$")

password = input("Password:  ")

if pattern.fullmatch(password):
    print("Password is Valid")

else:
    print("Password is Invalid")