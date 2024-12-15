from random import randint
from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
nums = [randint(1, 100) for _ in range(50)]

for num in nums:
    bst.insert(num)
bst.inorder_traversal()

for i in range(25):
    bst.delete(nums[i])

bst.inorder_traversal()