from stack import Stack
from queue_structure import Queue

def switch_biggest_in_queue_with_smallest_in_stack(target_stack: Stack, target_queue: Queue) -> Stack:
    helper_var = float('-inf')
    helper_queue = Queue(target_stack.size())

    # find biggest in queue
    queue_size = target_queue.size()
    for _ in range(queue_size):
        if target_queue.peek() > helper_var:
            helper_var = target_queue.peek()
        target_queue.enqueue(target_queue.dequeue())

    # store biggest in queue in target queue's peek place
    target_queue.enqueue(helper_var)
    for _ in range(queue_size):
        target_queue.enqueue(target_queue.dequeue())
    helper_var = float('inf')

    # find smallest in stack
    stack_size = target_stack.size()
    for _ in range(stack_size):
        if target_stack.peek() < helper_var:
            helper_var = target_stack.peek()
        helper_queue.enqueue(target_stack.pop())

    # move back elements from queue to stack with initial order
    while not helper_queue.isEmpty():
        if helper_queue.peek() == helper_var: # change min of stack with max of queue
            target_stack.push(target_queue.dequeue())
            helper_queue.dequeue()
            continue
        target_stack.push(helper_queue.dequeue())

    while not target_stack.isEmpty():
        helper_queue.enqueue(target_stack.pop())
    while not helper_queue.isEmpty():
        target_stack.push(helper_queue.dequeue())

    return target_stack


q = Queue()
q.enqueue(8)
q.enqueue(5)
q.enqueue(10)
q.enqueue(2)

s = Stack()
s.push(3)
s.push(6)
s.push(-5)
s.push(7)

switch_biggest_in_queue_with_smallest_in_stack(s, q).print()