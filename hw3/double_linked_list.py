from node import DoublyNode

class DoubleLinkedList:
    def __init__(self, max_size: int = float('inf')) -> None:
        self._head = None
        self._tail = None
        self._size = -1
        self._max_size = max_size

    def is_empty(self) -> bool: # O(1)
        return self._size == -1

    def is_full(self) -> bool: # O(1)
        return self._size >= self._max_size

    def size(self) -> int: # O(1)
        return self._size + 1

    def insert_at_beginning(self, data: any) -> None: # O(1)
        if self.is_empty():
            self._head = self._tail = DoublyNode(data)
        elif self.is_full():
            raise Exception("DoubleLinkedList is full, you can not insert at the beginning of list!")
        else:
            new_node = DoublyNode(data)
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def insert_at_end(self, data: any) -> None: # O(1)
        if self.is_empty():
            self._tail = self._head = DoublyNode(data)
        elif self.is_full():
            raise Exception("DoubleLinkedList is full, you can not insert at end of list!")
        else:
            new_node = DoublyNode(data)
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def insert_at_position(self, index: int, data: any) -> None: # O(n)
        if index > self.size() or index < 0:
            raise Exception("Index out of range!")
        if self.is_full():
            raise Exception("DoubleLinkedList is full, you can not insert at any position of list!")
        if index == 0:
            self.insert_at_beginning(data)
            return None
        elif index == self.size():
            self.insert_at_end(data)
            return None

        new_node = DoublyNode(data)
        temp_node = self._head
        while index:
            temp_node = temp_node.next
            index -= 1

        new_node.next = temp_node
        new_node.prev = temp_node.prev
        temp_node.prev.next = new_node
        temp_node.prev = new_node
        self._size += 1

    def delete_by_position(self, index: int) -> DoublyNode: # O(n)
        if index > self._size or index < 0:
            raise Exception("Index out of range!")
        if self.is_empty():
            raise Exception("DoubleLinkedList is empty! you can not delete from any position!")

        if index == 0:
            temp_node = self._head
            if self.size() == 1:
                self._head = self._tail = None
            else:
                self._head = self._head.next
                self._head.prev = None
        elif index == self._size:
            temp_node = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
        else:
            temp_node = self._head
            while index:
                temp_node = temp_node.next
                index -= 1

            temp_node.prev.next = temp_node.next
            temp_node.next.prev = temp_node.prev
        self._size -= 1
        return temp_node

    def delete_by_value(self, value: any) -> DoublyNode: # O(n)
        if self.is_empty():
            raise Exception("DoubleLinkedList is empty! you can not delete from any position!")

        temp_node = self._head
        while temp_node is not None and temp_node.data != value:
            temp_node = temp_node.next
        
        if temp_node.data != value:
            raise Exception("No Node Found With This Value!")

        if self._head == temp_node and self._tail == temp_node:
            self._head = None
            self._tail = None
        elif self._head == temp_node:
            self._head = self._head.next
            if self._head:
                self._head.prev = None
        elif self._tail == temp_node:
            self._tail = self._tail.prev
            if self._tail:
                self._tail.next = None
        else:
            temp_node.prev.next = temp_node.next
            temp_node.next.prev = temp_node.prev

        self._size -= 1
        return temp_node

    def search(self, key: any) -> bool: # O(n)
        temp_node = self._head
        while temp_node:
            if temp_node.data == key:
                return True
            temp_node = temp_node.next
        return False

    def reverse(self) -> None: # O(n)
        if self.is_empty():
            return None

        current = self._head
        prev = None
        self._tail = self._head

        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        self._head = prev

    def display(self) -> None: # O(n)
        temp = self._head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print(None)

    def removegt(self, val: any) -> None:  # O(n)
        temp_node = self._head
        i = 0
        while temp_node:
            if temp_node.data > val:
                self.delete_by_position(i)
            else:
                i += 1
            temp_node = temp_node.next

    def count(self) -> int: # O(n), same as size function
        # return self.size()
        temp = self._head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    linked_list = DoubleLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(6)
    linked_list.display()
    linked_list.removegt(2)
    linked_list.display()
    linked_list.reverse()
    linked_list.display()
    print(linked_list.count())
    # linked_list.insert_at_beginning(3)
    # linked_list.insert_at_end(2)
    # linked_list.insert_at_beginning(1)
    # linked_list.insert_at_beginning(0)
    # linked_list.display()
    # linked_list.insert_at_position(3, 5)
    # linked_list.display()
    # linked_list.delete_by_position(4)
    # linked_list.display()
    # linked_list.delete_by_value(3)
    # linked_list.display()
    # print(linked_list.size())
    # print(linked_list.count())