#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        层次遍历，获取最后一层的节点。
        """
        q = [root]
        pre_q = q
        res = 0
        while q:
            tmp = []
            pre_q = q.copy()
            while q:
                node = q.pop()
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            q = tmp
        
        for node in pre_q:
            res += node.val
        return res
# @lc code=end

