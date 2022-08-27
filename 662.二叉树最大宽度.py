#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 对一个二叉树每个节点都进行标号
        # 根据其在完全二叉树中的位置，一个index号的节点，其左孩子为2*index 右孩子为2*Index+1
        res = 1
        q = [(root,1)]
        while q:
            tmp = []
            for node,index in q:
                if node.left:
                    tmp.append((node.left,2*index))
                if node.right:
                    tmp.append((node.right,2*index+1))
            res = max(res,q[-1][1] - q[0][1] +1)
            q = tmp
        return res
# @lc code=end

