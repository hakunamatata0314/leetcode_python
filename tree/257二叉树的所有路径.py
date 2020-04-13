'''
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        paths = []
        # 每次递归path都保留走过的路径
        def helper(root, path):
            if not root: return
            path += str(root.val)
            # 如果当前节点为叶子节点，就把路径加到答案中
            if not root.left and not root.right:
                paths.append(path)
            # 如果当前节点不是叶子节点，就继续递归
            else:
                path += '->'
                helper(root.left, path)
                helper(root.right, path)
        # 初始化path要用空字符串，才可以+=str
        helper(root, '')
        return paths