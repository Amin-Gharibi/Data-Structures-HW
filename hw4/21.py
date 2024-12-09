from random import randint
from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
nums = [randint(1, 100) for _ in range(50)]

for num in nums:
    bst.insert(num)
bst.inorder_traversal()

for _ in range(randint(1, 50)):
    bst.delete(nums[randint(0, 49)])

bst.inorder_traversal()