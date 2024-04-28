def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

first = get_number("Enter first number: ")
second = get_number("Enter second number: ")
total = first + second

print(f"The sum of the numbers is {total}")
