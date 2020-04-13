'''
(Leetcode 617)  Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover 
the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two 
nodes overlap, then sum node values up as the new value of the merged node. Otherwise, 
the NOT null node will be used as the node of new tree.

Example 1:
Input:
    Tree 1     Tree 2
      1          2
    /   \      /   \
   3     2    1     3
  /            \     \ 
 5              4     7
Output: 
Merged tree:
      3 
    /   \
   4     5
  /  \    \      
 5    4    7       
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
