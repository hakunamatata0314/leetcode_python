'''
(Leetcode 700 ) Search in a Binary Search Tree
Given the root node of a binary search tree (BST) and a value. You need to find 
the node in the BST that the node's value equals the given value. Return the subtree 
rooted with that node. If such node doesn't exist, you should return NULL.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to search: 2
You should return this subtree:
      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, 
we should return NULL.
Note that an empty tree is represented by NULL, therefore you would see the expected output
(serialized tree format) as [], not null.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # begins from the root and keeps looking the target val.
    # as a BST, the node at the left subtree always smaller than
    # the root while the right subtree always bigger.
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            # print(root)
            # here we need to return TreeNode instead of the list of the subtree
            return root
        elif root.val < val:
            # you should RETURN to run the recursion visiting all the TreeNodes
            # of the subtree, every "return root" makes up the TreeNodes
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)  
