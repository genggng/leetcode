#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if  depth == 1:
            # print("hello")
            new_root = TreeNode(val=val,left=root)
            # print(new_root)
            return new_root
        
        # 层次遍历
        q = [root]
        height = 1
        while q:
            if height == depth-1:
                break
            tmp = []
            while q:
                node = q.pop()
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            q = tmp
            height += 1
        # 此时q存储的是第depth-1层的所有节点
        for node in q:
            nodeleft = TreeNode(val=val,left=node.left)
            noderight = TreeNode(val=val,right=node.right)
            node.left = nodeleft
            node.right = noderight
        return root
        
# @lc code=end

