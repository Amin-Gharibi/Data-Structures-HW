from stack import Stack
from queue_structure import Queue

def func(main_stack: Stack) -> Stack:
    helper_queue = Queue()
    final_stack = Stack()

    while not main_stack.isEmpty():
        final_stack.push(main_stack.pop())
    while not final_stack.isEmpty():
        helper_queue.enqueue(final_stack.pop())
    while not helper_queue.isEmpty():
        final_stack.push(helper_queue.dequeue())

    return final_stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
func(s).print()