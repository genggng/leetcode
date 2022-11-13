#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node,tmp):
            if not node.left and not node.right:
                res.append(tmp)
            if node.left:
                dfs(node.left,tmp+"->"+str(node.left.val))
            if node.right:
                dfs(node.right,tmp+"->"+str(node.right.val))
        dfs(root,str(root.val))
        return res 
# @lc code=end

