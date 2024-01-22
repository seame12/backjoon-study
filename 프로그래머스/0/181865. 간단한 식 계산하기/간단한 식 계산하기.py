def solution(binomial):
    elements = binomial.split()
    operand1 = int(elements[0])
    operator = elements[1]
    operand2 = int(elements[2])

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2

    return result