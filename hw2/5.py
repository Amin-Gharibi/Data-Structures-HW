from queue_structure import Queue

def sort_cwm(target_queue: Queue) -> Queue:
    men_queue = Queue(target_queue.size())
    women_queue = Queue(target_queue.size())
    children_queue = Queue(target_queue.size())

    final_queue = Queue(target_queue.size())

    while not target_queue.isEmpty():
        if target_queue.peek().startswith('m'):
            men_queue.enqueue(target_queue.dequeue())
        elif target_queue.peek().startswith('w'):
            women_queue.enqueue(target_queue.dequeue())
        elif target_queue.peek().startswith('c'):
            children_queue.enqueue(target_queue.dequeue())

    while not women_queue.isEmpty() or not men_queue.isEmpty() or not children_queue.isEmpty():
        if not children_queue.isEmpty():
            final_queue.enqueue(children_queue.dequeue())
        if not women_queue.isEmpty():
            final_queue.enqueue(women_queue.dequeue())
        if not men_queue.isEmpty():
            final_queue.enqueue(men_queue.dequeue())

    return final_queue


q = Queue(6)
q.enqueue('m1')
q.enqueue('m2')
q.enqueue('w1')
q.enqueue('c1')
q.enqueue('m3')
q.enqueue('c2')

sort_cwm(q).print()