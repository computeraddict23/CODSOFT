import random
import string

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(all_chars, k=length))

print("Your password is:", password)