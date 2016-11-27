#Simple Calculator Program by @Dewhallez

print("Welcome to the simple python calculator")
print("What is your name: ")
user_Name = input(">>")
print("Hello " + user_Name)

def add(x, y):
    return x+y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def percent(x, y):
    return (x/100) * y

def modulus(x, y):
    return x % y

#User inputs
print("Select an Operation. ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Reminder")
print("6.Percentage")


# Getting input and operation choice from user

user_Choice = input("Enter selection(1/2/3/4/5/6):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Printing out user inputs
print("You entered " +str(num1)+ " as the first number and "+str(num2)+ " as the second number")

#Addition 
if user_Choice == "1":
    print("Adding your numbers......")
    print("The sum of",num1, "+", num2, "is equal to",add(num1, num2))

#Subtraction
elif user_Choice == "2":
    print("Ok subtracting your numbers.....")
    print("The result of", num1, "-", num2, "is equal to",subtraction(num1, num2))

#Multiplication
elif user_Choice == "3":
    print("Multiplying your numbers.....")
    print("Multiplying", num1, "by", num2, "is equal to",multiplication(num1, num2))

#Division
elif user_Choice == "4":
    print("Dividing your numbers.....")
    print("Dividing", num1, "with", num2, "is equal to",division(num1, num2))

#Modulus/Reminder
elif user_Choice == "5":
    print("Getting the reminder for you.....")
    print("Modulus", num1, "after dividing by", num2, "is equal to",modulus(num1, num2))

#Percentage
elif user_Choice == "6":
    print("Calculating your percentage.....")
    print(num1, "percent of", num2, "is equal to",percent(num1, num2),"%")



