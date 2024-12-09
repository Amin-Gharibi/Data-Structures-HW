from double_linked_list import DoubleLinkedList

class QueueUsingDoubleLinkedList:
    def __init__(self, max_size: int = float('inf')) -> None:
        self.max_size = max_size
        self.linked_list = DoubleLinkedList(max_size)

    def is_empty(self) -> bool: # O(1)
        return self.linked_list.is_empty()

    def is_full(self) -> bool: # O(1)
        return self.linked_list.is_full()

    def size(self) -> int: # O(1)
        return self.linked_list.size()

    def enqueue(self, value) -> None: # O(1)
        if self.linked_list.is_full():
            raise Exception('Queue is full')
        self.linked_list.insert_at_beginning(value)

    def dequeue(self) -> any: # O(n)
        if self.linked_list.is_empty():
            raise Exception('Queue is empty')
        return self.linked_list.delete_by_position(self.linked_list.size() - 1).data

    def print(self) -> None: # O(n)
        self.linked_list.display()

class StackUsingDoubleLinkedList:
    def __init__(self, max_size: int = float('inf')) -> None:
        self.max_size = max_size
        self.linked_list = DoubleLinkedList(max_size)

    def is_empty(self) -> bool: # O(1)
        return self.linked_list.is_empty()

    def is_full(self) -> bool: # O(1)
        return self.linked_list.is_full()

    def size(self) -> int: # O(1)
        return self.linked_list.size()

    def push(self, value) -> None: # O(1)
        if self.linked_list.is_full():
            raise Exception('Stack is full')
        self.linked_list.insert_at_end(value)

    def pop(self) -> any: # O(n)
        if self.linked_list.is_empty():
            raise Exception('Stack is empty')
        return self.linked_list.delete_by_position(self.linked_list.size() - 1).data

    def print(self) -> None: # O(n)
        self.linked_list.display()

if __name__ == '__main__':
    # **** queue test
    # q = QueueUsingDoubleLinkedList()
    # q.enqueue(5)
    # q.enqueue(6)
    # q.enqueue(7)
    # q.enqueue(8)
    # q.print()
    # q.dequeue()
    # print(q.dequeue())
    # q.print()

    # **** stack test
    s = StackUsingDoubleLinkedList()
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.print()
    s.pop()
    print(s.pop())
    s.print()