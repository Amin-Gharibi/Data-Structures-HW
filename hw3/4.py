from linked_list import LinkedList
from node import SingleNode

class CustomDoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def recursive_reverse(self, node: SingleNode = None): # O(n)
        if node is None:
            node = self._head

        if node.next is None:
            self._head = node
            return
        self.recursive_reverse(node.next)
        node.next.next = node
        node.next = None

if __name__ == '__main__':
    l = CustomDoubleLinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.display()
    l.recursive_reverse()
    l.display()
