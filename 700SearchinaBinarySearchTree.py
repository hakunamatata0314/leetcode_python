'''
    Jiayao Li
    CS 5001
    Hw 9
    April 11st, 2020
    Programming #2 (Leetcode 700 ) Search in a Binary Search Tree
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
