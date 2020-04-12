'''
    Jiayao Li
    CS 5001
    Hw 9
    April 11st, 2020
    Programming #1 (Leetcode 617)  Merge Two Binary Trees
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # when both t1 and t2 has value, add t2.val to t1.val
        if t1 and t2:
            t1.val += t2.val
            # here should assign the new TreeNode to the t1. Without the
            # assignment, when it comes to the case the t1.left or t1.right
            # is None, the t1 child node will not be created.
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        # when t1 or t2 has value, return the one has val(the TreeNode only
        # exists when it has value), and assign it to t1 after calling the
        # recursion.
        else:
            return t1 or t2
