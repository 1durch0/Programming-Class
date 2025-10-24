print("This is a calculator!")
print("You can add, subtract, multiply, divide numbers and find the modulus!")
print("Use add for addition, sub for substraction, multiply for multiplication, divide for division, mod for modulus")
def add(x, y):
    return int(x) + int(y)
def sub(x, y):
    return int(x) - int(y)
def mul(x, y):
    return int(x) * int(y)
def div(x, y):
    return int(x) / int(y)
def mod(x, y):
    return int(x) % int(y)

def calc():
    operator = str(input("Write your operator here: "))
    match operator:
        case 'add':
            return add(input("Put your first number here: "), input("Put your second number here: "))
        case 'sub':
            return sub(input("Put your first number here: "), input("Put your second number here: "))
        case 'multiply':
            return mul(input("Put your first number here: "), input("Put your second number here: "))
        case 'multiply':
            return mul(input("Put your first number here: "), input("Put your second number here: "))
        case 'divide':
            return div(input("Put your first number here: "), input("Put your second number here: "))
        case 'mod':
            return mod(input("Put your first number here: "), input("Put your second number here: "))
        case _:
            return("Error: wrong input")

print(calc())
