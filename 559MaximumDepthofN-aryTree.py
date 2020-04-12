'''
(Leetcode 559)  Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Example 1:
      1
    / | \
   3  2  4
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
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return len(result)
