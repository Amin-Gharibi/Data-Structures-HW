from math import floor, log2
from node import Node


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    # ** PRIVATE FUNCTIONS **
    def __inorder_traversal(self, root: Node) -> None:
        if root is None:
            return

        self.__inorder_traversal(root.left)
        print(root.data, end=" -> ")
        self.__inorder_traversal(root.right)

    def __preorder_traversal(self, root: Node) -> None:
        if root is None:
            return

        print(root.data, end=" -> ")
        self.__preorder_traversal(root.left)
        self.__preorder_traversal(root.right)

    def __postorder_traversal(self, root: Node) -> None:
        if root is None:
            return

        self.__postorder_traversal(root.left)
        self.__postorder_traversal(root.right)
        print(root.data, end=" -> ")

    @staticmethod
    def __level_order_traversal(root: Node) -> None:
        if root is None:
            return
        queue = [root]

        while len(queue) > 0:
            print(queue[0].data, end=' -> ')
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def __insert_recursive(self, root: Node, value: any) -> Node:
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.__insert_recursive(root.left, value)
        else:
            root.right = self.__insert_recursive(root.right, value)
        return root

    def __delete_recursive(self, root: Node, key: any) -> Node | None:
        if root is None:
            return root
        if key < root.data:
            root.left = self.__delete_recursive(root.left, key)
        elif key > root.data:
            root.right = self.__delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.__find_min(root.right)
            root.data = temp.data
            root.right = self.__delete_recursive(root.right, temp.data)
        return root

    def __search(self, root: Node, value: any) -> bool:
        if root is None or root.data == value:
            return bool(root)
        if value < root.data:
            return self.__search(root.left, value)
        return self.__search(root.right, value)

    def __calculate_height(self, node: Node) -> int:
        if node is None:
            return -1

        left_height = self.__calculate_height(node.left)
        right_height = self.__calculate_height(node.right)

        return max(left_height, right_height) + 1

    @staticmethod
    def __find_min(root: Node) -> Node:
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr

    # ** PUBLIC FUNCTIONS **
    def insert(self, value: any) -> None:
        self._root = self.__insert_recursive(self._root, value)
        self._size += 1

    def delete(self, key: any) -> None:
        self._root = self.__delete_recursive(self._root, key)
        self._size -= 1

    def search(self, key: any) -> bool:
        return self.__search(self._root, key)

    def inorder_traversal(self) -> None:
        self.__inorder_traversal(self._root)
        print(None)

    def preorder_traversal(self) -> None:
        self.__preorder_traversal(self._root)
        print(None)

    def postorder_traversal(self) -> None:
        self.__postorder_traversal(self._root)
        print(None)

    def level_order_traversal(self) -> None:
        self.__level_order_traversal(self._root)
        print(None)

    def calculate_height(self) -> int:
        return self.__calculate_height(self._root)



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.inorder_traversal()
    bst.preorder_traversal()
    bst.postorder_traversal()
    bst.level_order_traversal()
    print(bst.search(6))
    bst.delete(2)
    bst.level_order_traversal()
    print(bst.height())