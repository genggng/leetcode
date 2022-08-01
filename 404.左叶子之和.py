#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root,loc):
            nonlocal res 
            if not root: return
            if loc == "left" and not root.left and not root.right:
                res += root.val
                return
            dfs(root.left,"left")
            dfs(root.right,"right")

        dfs(root,"none")

        return res
            
        
# @lc code=end

