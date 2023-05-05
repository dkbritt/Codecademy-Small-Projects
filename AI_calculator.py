# A simple calculator written in Python

# Define some functions to perform the basic arithmetic operations
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

# Get the user's input for the first number
print("Enter the first number:")
first_number = int(input())

# Get the user's input for the second number
print("Enter the second number:")
second_number = int(input())

# Display a menu of options
print("What operation would you like to perform?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get the user's choice
choice = int(input())

# Perform the operation
if choice == 1:
  print(first_number, "+", second_number, "=", add(first_number, second_number))
elif choice == 2:
  print(first_number, "-", second_number, "=", subtract(first_number, second_number))
elif choice == 3:
  print(first_number, "*", second_number, "=", multiply(first_number, second_number))
elif choice == 4:
  print(first_number, "/", second_number, "=", divide(first_number, second_number))
else:
  print("Invalid choice.")