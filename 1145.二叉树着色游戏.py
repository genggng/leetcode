#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """
        以选定节点作为原始节点，查找三个子区域的节点数。
        """
        xNode = None
        def get_tree_size(node):
            # 返回node的元素树木
            if not node:
                return 0
            if node.val == x:
                nonlocal xNode
                xNode = node  # 顺便找到x节点在哪
            return 1 + get_tree_size(node.left) + get_tree_size(node.right)
        
        get_tree_size(root) #找到x节点
        leftsize = get_tree_size(xNode.left)
        if leftsize >= (n+1)//2:
            return True
        rightsize = get_tree_size(xNode.right)
        if rightsize >= (n+1)//2:
            return True
        return (n - 1 - leftsize - rightsize) >= (n+1)//2
# @lc code=end

