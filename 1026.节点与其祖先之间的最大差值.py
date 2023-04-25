#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#

# @lc code=start
# Definition for a binary tree node.
# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root,min_grand,max_grand):
            # 传入一棵子树，已经子树的最大和最小祖先
            if not root:
                return
            val = root.val
            nonlocal res
            v1 = abs(val-min_grand)
            v2 = abs(val-max_grand)
            res = max([res,v1,v2])
            min_grand = min(min_grand,val)
            max_grand = max(max_grand,val)
            dfs(root.left,min_grand,max_grand)
            dfs(root.right,min_grand,max_grand)
        dfs(root,min_grand=root.val,max_grand=root.val)
        return res
# @lc code=end
tree = TreeNode(1,None,TreeNode(2,None,TreeNode(0,TreeNode(3,None,None),None)))

print(Solution().maxAncestorDiff(tree))


