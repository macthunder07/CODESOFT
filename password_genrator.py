import random
import string

def create_password(size):
    if size < 4:
        return "Password length should be at least 4 characters."
    pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(pool, k=size))

while True:
    user_input = input("Enter desired password length (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting...")
        break

    if user_input.isdigit():
        length = int(user_input)
        result = create_password(length)
        if "Password" not in result:
            print("Generated Password:", result)
        else:
            print(result)
    else:
        print("Please enter a valid number.")
