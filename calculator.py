print("SIMPLE CALCULATOR PROGRAM")
variable1 = int(input("Enter your first digit: "))
variable2 = int(input("Enter your second digit: "))
print("CHOOSE YOUR OPERATOR (+, -, *, /): ", end="")

match input():
        case "+":
            x = f"{variable1} + {variable2} = {variable1 + variable2}"
            print(x)
        case "-":
            x = f"{variable1} - {variable2} = {variable1 - variable2}"
            print(x)
        case "*":
            x = f"{variable1} * {variable2} = {variable1 * variable2}"
            print(x)
        case "/":
            if variable2 != 0:
                result = variable1 / variable2
                x = f"{variable1} / {variable2} = {round(result)}"  
                print(x)
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operator. choose from +, -, *, /")  