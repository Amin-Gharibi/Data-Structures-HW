from node import Node
from binary_search_tree import BinarySearchTree

class CustomBST(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def __remove_nodes_gt(self, root: Node, key: int) -> Node | None:
        if root is None:
            return None

        root.left = self.__remove_nodes_gt(root.left, key)
        root.right = self.__remove_nodes_gt(root.right, key)

        if root.data > key:
            return root.left
        return root

    def remove_nodes_gt(self, pivot: int) -> None:
        self.__remove_nodes_gt(self._root, pivot)


if __name__ == '__main__':
    bst = CustomBST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(10)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(12)
    bst.insert(8)
    bst.insert(9)
    bst.insert(18)
    bst.insert(20)
    bst.inorder_traversal()
    bst.remove_nodes_gt(10)
    bst.inorder_traversal()
