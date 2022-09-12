#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pickle import HIGHEST_PROTOCOL


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        二叉搜索树：左子树的值都比根节点小，右子树的值都比根节点大
        在删减过程中：
            如果node>high,那么node.right 和 node可以删除掉，返回右子树的删选结果
            如果node<low,那么node.left 和node 可以删除掉，在左子树的删选结果
            如果 node in [low,high],那么node是符合条件的，返回返回左右子树的筛选结果作为左右子树
        """
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right,low,high)
        if root.val > high:
            return self.trimBST(root.left,low,high)
        
        # low <= root.val <= high
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root
# @lc code=end

