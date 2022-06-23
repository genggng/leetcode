#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        层次遍历
        关键点是如何判断是在同一层的节点。
        很简单，bfs队列中每行就是存储的同一层的所有节点。
        使用两个列表来分割两个层的节点。
        if not root: return []
        res = []
        bn = [root]
        while bn:
            res.append(max([x.val for x in bn]))
            tmp = []
            while bn:
                node = bn.pop()
                if node.left: tmp.append(node.left)
                if node.right:tmp.append(node.right)
            bn = tmp

        先序深度优先遍历
        使用curHeight记录当前所在的深度。
        并不是一次更新完一层，而是递归更新。
        """
        res = []
        def dfs(node,curHeight):
            if node is None:return
            if curHeight == len(res):
                res.append(node.val) # 该层的第一个节点
            else:
                res[curHeight] = max(res[curHeight],node.val) #更新height层最大值
            dfs(node.left,curHeight+1)
            dfs(node.right,curHeight+1)
        dfs(root,0)
        return res                

# @lc code=end

