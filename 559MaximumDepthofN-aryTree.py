'''
    Jiayao Li
    CS 5001
    Hw 9
    April 11st, 2020
    Programming #3 (Leetcode 559)  Maximum Depth of N-ary Tree
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
