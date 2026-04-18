import art
#n1 = int(input("What's the first number?: "))
#n2 = int(input("What's the second number?: "))

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

#TODO: Create a dictionary called operations that contains the 4 operation symbols as keys and the corresponding functions as values.
# keys = "+", "-", "*", "/"
# values = add, subtract, multiply, divide

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#TODO: Use the dictionary to calculate the result of 4 * 8 and print the result.

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

#should_accumulate = variable that will determine whether the calculator should continue calculating with the current answer or start a new calculation.
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

#Choice = variable that will store the user input to decide whether to continue calculating with the current answer or start a new calculation.
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
#20 new lines to clear the console
            calculator()

calculator()
