from stack import Stack

def count_valid_parentheses(text: str) -> int:
    stack = Stack(len(text))
    count = 0
    for c in text:
        if c == '(':
            stack.push(c)
        elif c == ')' and stack.peek():
            stack.pop()
            count += 1
    return count

txt = "(((data structures))))))))))((ds4031((ilam university))))"
print(count_valid_parentheses(txt))