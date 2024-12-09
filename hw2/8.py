from stack import Stack

def sort_stack(target_stack: Stack) -> Stack:
    sorted_stack = Stack(target_stack.size())
    temp_stack = Stack(target_stack.size())

    while not target_stack.isEmpty():
        current = target_stack.pop()

        while not sorted_stack.isEmpty() and sorted_stack.peek() > current:
            temp_stack.push(sorted_stack.pop())

        sorted_stack.push(current)

        while not temp_stack.isEmpty():
            sorted_stack.push(temp_stack.pop())

    return sorted_stack

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(7)
stack.push(3)
stack.push(5)
sort_stack(stack).print()
            
            
