from node import SingleNode

class LinkedList:
    def __init__(self, max_size: int = float('inf')) -> None:
        self._max_size = max_size
        self._head = None
        self._size = -1

    def is_empty(self) -> bool: # O(1)
        return self._size < 0

    def is_full(self) -> bool: # O(1)
        return self._size >= self._max_size - 1

    def size(self): # O(1) || O(n)
        # temp = self._head
        # count = 0
        # while temp:
        #     count += 1
        #     temp = temp.next
        # return count
        return self._size + 1

    def get_by_index(self, index: int) -> SingleNode: # O(n)
        temp = self._head
        while index:
            temp = temp.next
            index -= 1
        return temp

    def add(self, value: any, index: int = None) -> None: # O(n)
        if index is None:
            index = self.size()
        if index < 0 or index > self.size():
            raise Exception('Index out of range for adding!')
        if self.is_full():
            raise Exception('LinkedList is full')

        new_node = SingleNode(value)
        if index == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            temp = self._head
            while index > 1: # it's one so it would iterate until the one before the target index because the size is index + 1, and we start from head
                temp = temp.next
                index -= 1
            new_node.next = temp.next
            temp.next = new_node
        self._size += 1

    def remove(self, index: int = None) -> SingleNode: # O(n)
        if index is None:
            index = self._size
        if not (0 <= index < self.size()):
            raise Exception('Index out of range for removing!')
        if self.is_full():
            raise Exception('LinkedList is full')

        if index == 0:
            temp = self._head
            self._head = self._head.next
        else:
            temp = self._head
            while index > 1: # it's one so it would iterate until the one before the target index because the size is index + 1, and we start from head
                temp = temp.next
                index -= 1
            temp.next = temp.next and temp.next.next or None
        self._size -= 1
        return temp

    def swap(self, i: int, j: int) -> None: # O(i) + O(j) => O(n)
        if not (0 <= i < self.size() and 0 <= j < self.size()):
            raise Exception('Index out of range for swapping!')
        if i == j:
            return

        prev_i = None
        curr_i = self._head
        while i:
            prev_i = curr_i
            curr_i = curr_i.next
            i -= 1
        prev_j = None
        curr_j = self._head
        while j:
            prev_j = curr_j
            curr_j = curr_j.next
            j -= 1

        if prev_i:
            prev_i.next = curr_j
        else:
            self._head = curr_j
        if prev_j:
            prev_j.next = curr_i
        else:
            self._head = curr_i

        curr_i.next, curr_j.next = curr_j.next, curr_i.next

    def remove_all(self) -> None: # O(1)
        self._head = None

    def display(self) -> None: # O(n)
        temp = self._head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(0)
    linked_list.add(2)
    linked_list.add(3, 0)
    linked_list.add(5, 2)
    linked_list.display()
    linked_list.remove()
    linked_list.display()
    linked_list.swap(0, 2)
    linked_list.display()
    linked_list.remove_all()
    linked_list.display()