def perform_operation(num1, num2, option):
    operations = {
        "1": ("Sum is:", num1 + num2),
        "2": ("Difference is:", num1 - num2),
        "3": ("Product is:", num1 * num2),
        "4": ("Division is:", num1 / num2 if num2 != 0 else "undefined (division by zero)"),
        "5": ("Average is:", (num1 + num2) / 2)
    }

    if option in operations:
        label, result = operations[option]
        print(label, result)
    else:
        print("You entered an invalid operator")

def start_calculator():
    while True:
        print("\nSelect an operation:")
        print("1. Sum")
        print("2. Difference")
        print("3. Product")
        print("4. Division")
        print("5. Average")
        print("6. Exit")

        user_choice = input("Enter your choice (1-6): ")

        if user_choice == "6":
            print("Exiting...")
            break

        try:
            val1 = float(input("Enter first number: "))
            val2 = float(input("Enter second number: "))
            perform_operation(val1, val2, user_choice)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    start_calculator()
