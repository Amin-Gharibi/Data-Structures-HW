from stack import Stack
from queue_structure import Queue


def remove_min(target_stack: Stack) -> None:
    helper_queue = Queue(target_stack.size())
    min_elem = float('inf')

    while not target_stack.isEmpty(): # find the min elem and move all elem to the queue
        elem = target_stack.pop()
        if elem < min_elem:
            min_elem = elem
        helper_queue.enqueue(elem)

    count = helper_queue.size()
    for _ in range(count): # move all elements except the min to the stack
        elem = helper_queue.dequeue()
        if elem == min_elem:
            continue
        target_stack.push(elem)

    # the 2 bottom loops are to set the sorting as it was at first
    while not target_stack.isEmpty(): # move final elems to the queue
        helper_queue.enqueue(target_stack.pop())

    while not helper_queue.isEmpty(): # move back final elems to the stack
        target_stack.push(helper_queue.dequeue())


s = Stack(5)
s.push(8)
s.push(5)
s.push(2)
s.push(10)

print("Stack before remove: ", end="")
s.print()
remove_min(s)
print("Stack after remove: ", end="")
s.print()
