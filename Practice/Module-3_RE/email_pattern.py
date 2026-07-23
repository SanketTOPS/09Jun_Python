import re

#sanket@gmail.com
email=input("Enter an email:")

email_pattern="^[a-z]+[@]+[a-z]+[\.]+[a-z]"
x=re.findall(email_pattern,email)

if x:
    print("Email is valid!")
else:
    print("Error!Invalid Email...")