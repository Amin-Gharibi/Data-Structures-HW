from linked_list import LinkedList

class CustomLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def remove_m_nodes_after_each_n_nodes(self, n: int, m: int) -> None: # O(N/(n+m) * (n+m)) => O(N)
        current = self._head
        while current: # O(N/(n+m)), N is len of linked-list
            for _ in range(n - 1): # O(n) ----- because we start with the head itself so we should decrease it by 1
                if current is None:
                    return
                current = current.next
            if current is None:
                return

            temp = current
            for _ in range(m): # O(m)
                if temp.next is None:
                    break
                temp = temp.next
            if temp:
                current.next = temp.next
            current = current.next

if __name__ == '__main__':
    l = CustomLinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.display()
    l.remove_m_nodes_after_each_n_nodes(1, -1)
    l.display()
