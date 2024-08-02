# CALCULATOR 2
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 // num2

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option = input("Select operation(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if option == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif option == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif option == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif option == '4':
    print(num1, "//", num2, "=", divide(num1, num2))

else:
    print("Invalid input")