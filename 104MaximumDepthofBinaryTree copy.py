'''
(Leetcode 104)  Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # case 1: if there is no tree return depth=0 
        if not root:
            return 0
        # case 2: the tree has at least one node(the root), then initialize depth=1
        depth = 1
        # case 3: reach to the leaf node, where node.left and node.right are NULL.
        # return the depth of this path
        if not root.left and not root.right:
            return depth
        # after setting all the base case, design the recursion
        # every recursion need to pick the bigger depth and add the current node
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
 