'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common 
ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest 
common ancestor is defined between two nodes p and q as the lowest 
node in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # the key is to use the BST, children node at the left are smaller than the root,
    # and the right side are all bigger
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv, qv = p.val, q.val
        node = root
        # quit the while loop if finish visiting all the nodes
        while node:
            nv = node.val
            # if both pv and qv are smaller than nv, then the LCA must on the left tree
            if pv < nv and qv < nv:
                node = node.left
            # likewise, if both pv and qv are bigger than nv, then the LCA on the right tree
            elif pv > nv and qv > nv:
                node = node.right
            # if the nv is between pv and qv, that means finding the LCA
            else:
                return node

# use recursion
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         rv, pv, qv = root.val, p.val, q.val
#         if pv < rv and qv < rv:
#             return lowestCommonAncestor(root.left, p, q)
#         elif pv > rv and qv > rv:
#             return lowestCommonAncestor(root.right, p, q)
#         else:
#             return root