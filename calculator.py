result = 0

def calculate(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
        return result
    elif operator == '-':
        result = num1 - num2
        return result
    elif operator == '*':
        result = num1 * num2
        return result
    elif operator == '/':
        result = num1 / num2
        return result
    else:
        result = 'Invalid operator'
        return result

print(calculate(2, '/', 3)) # Change the numbers, operator
