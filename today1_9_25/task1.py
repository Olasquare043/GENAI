import math
# Simple Calculator Program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        result=(a / b)
        return f"{result:.2f}"
    else:
        return "Error: Division by zero"
# Function for raise to power of first nnumber by second
def power(a, b):
        return a ** b

# Function for square root
def square_root(a):
        result=math.sqrt(a)
        return f"{result:.2f}"


taskCon="y"
while(taskCon=="y"):
    print ("==========================================================")
    print ("=========== Welcome to Olasquare my calculator ===========")
    print ("==========================================================")
    print("")
    # Display operation options to the user
    print("Select operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. Square root")

    # Take input from the user for operation choice
    choice = input("Enter choice (1/2/3/4/5/6): ")
    # Get the number as input from the user
    if choice =='6':
        num1 = float(input("Enter the number: "))
    elif choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid input")
    else:
    # Get two numbers as input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    # Perform calculation based on user's choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2)) 
    elif choice == '6':
        print("Result:", square_root(num1))
    taskCon = input(f"""Do you want to perfform another task? Press 'y' to continue, press any key to terminate: """)
    print("")
print ("")
print ("")
print ("==========================================================")
print ("=================Thanks for using my calculator===========")
print ("==========================================================")