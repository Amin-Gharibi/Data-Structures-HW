from queue_structure import Queue

def switch_first_and_last_elem(target_queue: Queue) -> Queue:
    helper_queue = Queue(target_queue.size())

    first_elem = target_queue.dequeue()
    while target_queue.size() > 1:
        helper_queue.enqueue(target_queue.dequeue())
    helper_queue.enqueue(first_elem)

    while not helper_queue.isEmpty():
        target_queue.enqueue(helper_queue.dequeue())

    return target_queue

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.print()
switch_first_and_last_elem(q).print()