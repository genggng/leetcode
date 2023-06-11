#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (71.30%)
# Likes:    1063
# Dislikes: 0
# Total Accepted:    845.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,null,2,3]'
#
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[1,2]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
# 
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
# 
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代法，使用栈
        if not root:
            return []
        s = [root]
        res = []
        while s:
            cur = s.pop()
            res.append(cur.val)
            # 先进右树，再进左数。这样出栈就是左->右
            if cur.right:
                s.append(cur.right)
            if cur.left:
                s.append(cur.left)
        return res
            

# @lc code=end

