def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter operation number (1-4): ")

        if choice in {'1', '2', '3', '4'}:
            choice = int(choice)

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)

            print("Result:", result)

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
    like = input("Do you like the calculator? (y/n): ").lower()
    if like == 'n':
        print("THANK YOU FOR USING VARNI'S CALCULATOR")
    else:
        print("Great! I'm glad you like it.")
