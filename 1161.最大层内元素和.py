#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        层次遍历
        """
        q = [root]
        max_num = -float("inf")
        res = -1
        i = 1
        while q:
            tmp = []
            sum = 0
            for node in q:
                sum += node.val
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            if sum > max_num:
                res = i
                max_num = sum
            i += 1
            q = tmp
        return res
# @lc code=end

