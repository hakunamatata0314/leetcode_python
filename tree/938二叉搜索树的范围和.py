'''
938. 二叉搜索树的范围和
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
（求出所有 X >= L 且 X <= R 的值的和）
二叉搜索树保证具有唯一的值。

示例 1：
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
 
提示：
树中的结点数量最多为 10000 个。
最终的答案保证小于 2^31。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # 不加self会报错：本地变量res在赋值前引用
        self.res = 0
        # dfs 里不用return，因为直接把res更改了
        def dfs(root):
            if not root: return
            val = root.val
            if val >= L and val <= R:
                self.res += val
            if val < R:
                dfs(root.right)
            if val > L:
                dfs(root.left)
        dfs(root)
        return self.res

# # 用栈
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         ans = 0
#         stack = [root]
#         while stack:
#             root = stack.pop()
#             if root:
#                 if L <= root.val <= R:
#                     ans += root.val
#                 if L < root.val:
#                     stack.append(root.left)
#                 if R > root.val:
#                     stack.append(root.right)
#         return ans