#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (58.71%)
# Likes:    2393
# Dislikes: 0
# Total Accepted:    816.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            t = []
            level = []
            for node in q:
                if node.left:
                    t.append(node.left)
                    level.append(node.left.val)
                else:
                    level.append(999)
                if node.right:
                    t.append(node.right)
                    level.append(node.right.val)
                else:
                    level.append(999)
            n = len(level)
            if level[:n//2] != level[n//2:][::-1]:
                return False
            q = t
        return True
# @lc code=end
tree = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(4)))
print(Solution().isSymmetric(tree))

