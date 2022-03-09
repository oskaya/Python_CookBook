import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation_dictionary = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(logo.logo)

n1 = int(input("Type first number: "))
for key in operation_dictionary:
    print(key)

operation = input("Pick an operation: ")
function_to_use=operation_dictionary[operation]
n2 = int(input("Type second number: "))

answer = function_to_use(n1,n2)

print(f"{n1} {operation} {n2} is  = {answer}")