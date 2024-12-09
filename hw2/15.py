from stack import Stack

def infix_to_postfix(expression: str) -> str:
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }
    stack = Stack(len(expression))
    postfix_expression = ''

    i = 0
    while i < len(expression):
        if expression[i].isdigit():  # if c is part of an operand
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            postfix_expression += num + ' '
            continue

        elif expression[i] == '(':
            stack.push(expression[i])

        elif expression[i] == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                postfix_expression += stack.pop() + ' '
            stack.pop()

        else:  # if c is operator
            while not stack.isEmpty() and stack.peek() != '(' and precedence[stack.peek()] >= precedence[expression[i]]:
                postfix_expression += stack.pop() + ' '
            stack.push(expression[i])
        i += 1
    
    while not stack.isEmpty():
        postfix_expression += stack.pop() + ' '
    
    return postfix_expression.strip()

def calc_postfix(expression: str) -> int:
    stack = Stack(len(expression))
    operators = ["+", "-", "*", "/", "^"]

    for c in expression.split(" "):
        if c not in operators:
            stack.push(int(c))
        else:
            s = stack.pop()
            f = stack.pop()
            match c:
                case '+':
                    stack.push(f+s)
                case '-':
                    stack.push(f-s)
                case '*':
                    stack.push(f*s)
                case '/':
                    stack.push(f//s)
                case '^':
                    stack.push(f**s)
    
    return stack.pop()


postfix = infix_to_postfix("(10+4)*(4+2)")
print(postfix)
result = calc_postfix(postfix)
print(result)