# Simple Calculator Program by @Dewhallez

# Functions
def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def percent(x, y):
    return (x / 100) * y


def modulus(x, y):
    return x % y


# Greetings
print("Welcome to the simple python calculator")
user_Name = input("What is your name: ")
print("Welcome", user_Name)

while True:

    # User inputs
    print("\nSelect an Operation. \n")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Remainder")
    print("6: Percentage")
    print("7: Exit \n")

    # Getting input and operation choice from user
    user_choice = int(input("Enter your choice: "))

    # Getting numbers.
    if user_choice in range(1, 7):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Printing out user inputs
        print(
            "You entered", num1, "as the first number and", num2, "as the second number"
        )
    print()

    # Addition
    if user_choice == 1:
        print("Adding your numbers")
        print("The sum of", num1, "+", num2, "is", add(num1, num2))

    # Subtraction
    elif user_choice == 2:
        print("subtracting your numbers")
        print("The result of", num1, "-", num2, "is", subtraction(num1, num2))

    # Multiplication
    elif user_choice == 3:
        print("Multiplying your numbers")
        print(num1, "into", num2, "is", multiplication(num1, num2))

    # Division
    elif user_choice == 4:
        print("Dividing your numbers")
        print(num1, "divided by", num2, "is", division(num1, num2))

    # Modulus/Reminder
    elif user_choice == 5:
        print("Getting the reminder for you")
        print("Reminder of", num1, "divided by", num2, "is", modulus(num1, num2))

    # Percentage
    elif user_choice == 6:
        print("Calculating your percentage")
        print(num1, "percent of", num2, "is", percent(num1, num2), "%")

    elif user_choice == 7:
        print("Thank you for using my simple calculator program", user_Name)
        break

    else:
        print("Invalid Choice!")
