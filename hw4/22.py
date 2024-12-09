def find_preorder_traversal(inorder_traversal, postorder_traversal):
    if not inorder_traversal or not postorder_traversal:
        return []
    root = postorder_traversal[-1]
    root_index = inorder_traversal.index(root)

    left_inorder = inorder_traversal[:root_index]
    right_inorder = inorder_traversal[root_index + 1:]

    left_postorder = postorder_traversal[:len(left_inorder)]
    right_postorder = postorder_traversal[len(left_inorder):-1]

    preorder = [root] + find_preorder_traversal(left_inorder, left_postorder) + find_preorder_traversal(right_inorder, right_postorder)
    return preorder


inorder_traversal = [1,2,3,4,5,6]
postorder_traversal = [1,3,2,6,5,4]
preorder_traversal = find_preorder_traversal(inorder_traversal, postorder_traversal)

print(inorder_traversal)
print(postorder_traversal)
print(preorder_traversal)