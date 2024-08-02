
def check_number(num):
    try:
        return int(num)
    except:
        print("This is not a valid number please try again")
        main()

def main():
    while True:
        num1 = input("please enter the first number in your operation:")
        num1 = check_number(num1)
        num2 = input("please enter the second number in your operation:")
        num2 = check_number(num2)
        print("Which operation would you like to do?")
        print(f"{num1}+{num2}=?")
        print(f"{num1}-{num2}=?")
        print(f"{num1}*{num2}=?")
        print(f"{num1}/{num2}=?")
        operation = input("Please choose one: (+,-,*,/):")
        calculate(num1,num2,operation)

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2 

def divide(num1,num2):
    if num1 == 0 or num2 == 0:
        return "You cannot divide a number by 0, please try again."
    else:
        return num1/num2

def calculate(num1,num2,operation):
    if operation == '+':
        print(add(num1,num2))
    elif operation == '-':
        print(subtract(num1,num2))
    elif operation == '*':
        print(multiply(num1,num2))
    elif operation == '/':
        value = divide(num1,num2)
        if type(value) == str:
            print(value)
        else:
            print(value)

main()