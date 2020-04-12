'''
(Leetcode 111) Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from 
the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # case 1: if there is no tree return depth=0
        if not root:
            return 0
        # case 2: the tree has at least one node and then initialize depth=1
        depth = 1
        # case 3:reach to the leaf node, where node.left and node.right are NULL.
        # return the depth of this path
        if not root.left and not root.right:
            return depth
        # case 4: if the tree is unbalanced from the root, like {1,2,null}, root.right
        # is NULL, then return depth=depth(root)+depth(root.left)=1+1=2 instead of 
        # depth(root)=1. Likewise, when root.left is NULL, return 1+1=2
        elif not root.left or not root.right:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        # case 5: more childern nodes to traverse
        # design the recursion to pick the smaller depthand add the current node
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
