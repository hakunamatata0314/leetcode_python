'''
(Leetcode 559)  Maximum Depth of N-ary Tree
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Example 1:
        1
     /  |  \
    3   2   4
   / \
  5   6
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        # use a queue to pop() and extend() traversing each level of the tree
        # initialize with the root node
        queue = collections.deque([root])
        # use a list to store the childern node of each level, e.g.[[1],]
        result = []
        # quit the while loop when finish visiting all the nodes
        while queue:
            # initialize the level list at the beginning to visiting the nodes
            # at the same level
            level = []
            # begin the for loop to visit the same level nodes
            for i in range(len(queue)):
                # pop from the left, e.g. node=3, node=2, node=4
                node = queue.popleft()
                # store the val of the nodes in the same level within a list,e.g. level=[3,2,4]
                level.append(node.val)
                # extend the list of all the childern of the same level,
                # and quit the for loop, e.g. queue=([5,6])
                queue.extend(node.children)
            # append the whole val list of the same level to result, e.g.[[1],[3,2,4],[5,6]]
            result.append(level)
        # after visiting all levels, return the level of the tree which is the maximum depth
        return len(result)
