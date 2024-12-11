import re

# Verfication_Email

user_email = input("Please enter your email: ")

verfication_email = re.findall(r"^[a-z0-9]+@[a-z0-9]+\.[com|net]+$", user_email)
emails = []

if verfication_email != []:
    print("Email Added")
    emails.append(user_email)
    for email in emails:
        print(email)

else:
    print("This is an invalid email")



# Verfication_Site

is_site = re.search(r"^(https?://)(www.)(\w+)(.com|.net|.info|.me)$", "https://www.basel.com")

if is_site:
    print("This is a valid site")
    print(is_site.span())
    print(is_site.string)
    print(is_site.group())
else:
    print("This is an invalid site")



# Verfication_Phone_Number

is_phone_number = re.search(r"^(\d{3})-?\s?(\d{4}) (\d{3}|\(\d{3}\))$", "123-2025 (222)")

if is_phone_number:
    print("This is a valid phone number")
    print(is_phone_number.span())
    print(is_phone_number.string)
    print(is_phone_number.group())
else:
    print("This is an invalid phone number")