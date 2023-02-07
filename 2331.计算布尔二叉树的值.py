#
# @lc app=leetcode.cn id=2331 lang=python3
#
# [2331] 计算布尔二叉树的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return bool(root.val)
        else:
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            if root.val == 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
# @lc code=end

