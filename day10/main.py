import art

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

print(art.logo)
result = float(input("What is the first number? "))
done = False

while not done:
    a = result
    b = float(input("What is the next number? "))
    operation = input("What is your operation? ")
    result = operations[operation](a, b)
    print(f"Your result is {a} {operation} {b} = {result}")
    user_input = input("Do you want to make another operation with this number? Type 'y' if yes, 'r' to reset to new numbers or anything else to leave. ").lower()
    if user_input == 'r':
        result = float(input("What is the first number? "))
    elif user_input != 'y':
        done = True
