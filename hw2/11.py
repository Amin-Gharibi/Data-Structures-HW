from stack import Stack

text = input("Enter some text: ")
stack = Stack(len(text))

def dump_stack():
    while not stack.isEmpty():
        temp = stack.pop()
        print(temp, end="")


for c in text:
    if c == ' ':
        dump_stack()
        print(" ", end="")
    else:
        stack.push(c)

dump_stack()