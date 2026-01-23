expression = input("Expresson: ")
num1, op, num2 = expression.split(" ")
num1 = float(num1)
num2 = float(num2)

match op:
    case "+":
        answer = float(num1 + num2)
        answer = round(answer, 1)
        print(answer)
    case "-":
        answer = float(num1 - num2)
        answer = round(answer, 1)
        print(answer)
    case "*":
        answer = float(num1 * num2)
        answer = round(answer, 1)
        print(answer)
    case "/":
        answer = float(num1 / num2)
        answer = round(answer, 1)
        print(answer)