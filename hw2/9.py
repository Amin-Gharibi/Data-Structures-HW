from queue_structure import Queue
from stack import Stack

def sort_queue(target_queue: Queue) -> Queue:
    helper_stack = Stack(target_queue.size())

    while not target_queue.isEmpty():
        current = target_queue.dequeue()

        while not helper_stack.isEmpty() and helper_stack.peek() > current:
            target_queue.enqueue(helper_stack.pop())
        
        helper_stack.push(current)

    while not helper_stack.isEmpty():
        target_queue.enqueue(helper_stack.pop())

    return target_queue

queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(7)
queue.enqueue(5)
queue.enqueue(3)

sort_queue(queue).print()