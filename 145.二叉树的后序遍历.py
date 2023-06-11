#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s,res = [root],[]
        while s:
            i = s.pop()
            if isinstance(i,TreeNode):
                s += [i.val,i.right,i.left]
            elif isinstance(i,int):
                res.append(i)
        return res 

# @lc code=end

