from linked_list import LinkedList

class CustomLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def find_middle_node(self) -> any: # O(n)
        head = self._head
        for _ in range(self.size() // 2):
            head = head.next

        return head.data
        # fp = self._head
        # sp = self._head
        # while fp and fp.next:
        #     fp = fp.next.next
        #     sp = sp.next
        #
        # return sp.data

if __name__ == '__main__':
    l = CustomLinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.add(7)
    l.add(8)
    print(l.find_middle_node())