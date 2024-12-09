from double_linked_list import DoubleLinkedList

class CustomDoubleLinkedList(DoubleLinkedList):
    def __init__(self):
        super().__init__()

    def __str__(self): # O(n)
        current = self._head
        seen = set()
        pairs = []

        while current:
            complement = 10 - current.data
            if complement in seen:
                pairs.append((complement, current.data))
            seen.add(current.data)
            current = current.next
        return str(pairs)

if __name__ == '__main__':
    l = CustomDoubleLinkedList()
    l.insert_at_end(1)
    l.insert_at_end(2)
    l.insert_at_end(3)
    l.insert_at_end(4)
    l.insert_at_end(5)
    l.insert_at_end(6)
    l.insert_at_end(7)
    l.insert_at_end(8)
    l.insert_at_end(9)
    l.insert_at_end(10)
    l.insert_at_end(-5)
    l.insert_at_end(15)
    print(l)