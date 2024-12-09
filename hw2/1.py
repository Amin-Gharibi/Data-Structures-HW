from queue_structure import Queue

def reverse_queue(target_queue: Queue) -> None:
    if target_queue.isEmpty():
        return

    head = target_queue.dequeue()
    reverse_queue(target_queue)
    target_queue.enqueue(head)

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
reverse_queue(q)
q.print()