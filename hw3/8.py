from linked_list import LinkedList
from node import SingleNode

class CustomLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def custom_sort(self, pivot: int) -> None: # O(n)
        if not self._head or not self._head.next:
            return None

        less_node = SingleNode(0)    # nodes are defined to store the starting point of the chain
        greater_node = SingleNode(0) # nodes are defined to store the starting point of the chain
        less_pointer = less_node       # pointers are defined to store the end point of the chain
        greater_pointer = greater_node # pointers are defined to store the end point of the chain

        curr = self._head
        while curr:
            if curr.data >= pivot:
                greater_pointer.next = curr
                greater_pointer = greater_pointer.next
            else:
                less_pointer.next = curr
                less_pointer = less_pointer.next
            curr = curr.next

        less_pointer.next = greater_node.next # connect less containing chain to greater containing chain
        greater_pointer.next = None # if the last node that was added was pointing to another node then break the connection to prevent loop
        self._head = less_node.next

if __name__ == '__main__':
    l = CustomLinkedList()
    l.add(8)
    l.add(9)
    l.add(10)
    l.add(11)
    l.add(12)
    l.add(13)
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.display()
    l.custom_sort(4)
    l.display()