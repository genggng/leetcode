#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_num = -1
        max_index = -1
        for i,num in enumerate(nums):
            if num>max_num:
                max_num = num
                max_index = i
        root = TreeNode(max_num,left=self.constructMaximumBinaryTree(nums[:max_index]),right=self.constructMaximumBinaryTree(nums[max_index+1:]))
        return root
# @lc code=end

