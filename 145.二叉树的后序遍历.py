#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代法，维护一个栈
        # 将根节点入栈
        # 将左子树入栈
        # 将右子树入栈
        if not root: return list()
        stack = []
        res = []
        prev = None
        while root or stack:
            while root: #将左子树的根节点入栈
                stack.append(root)
                root = root.left
            root = stack.pop()  #左叶子节点
            if not root.right or root.right == prev:
                # prev的作用是将节点从右子树返回
                res.append(root.val)  #没有右子树，直接出栈左子树
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right  #展开右子树
        return res

# @lc code=end

