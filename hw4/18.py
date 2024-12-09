from node import Node
from binary_search_tree import BinarySearchTree

class CustomBST(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def __count_leaf_nodes(self, root: Node) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        count = self.__count_leaf_nodes(root.left) + self.__count_leaf_nodes(root.right)
        return count

    def count_leaf_nodes(self) -> int:
        return self.__count_leaf_nodes(self._root)


if __name__ == '__main__':
    bst = CustomBST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    print(bst.count_leaf_nodes())