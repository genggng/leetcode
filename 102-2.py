from typing import List,Optional

"""
6335. 二叉树的堂兄弟节点 II 显示英文描述 
给你一棵二叉树的根 root ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。

如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。

请你返回修改值之后，树的根 root 。

注意，一个节点的深度指的是从树根节点到这个节点经过的边数
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [[root]]
        total_val = root.val  #该层次所有元素的和。
        while q:
            t = []
            new_total_val = 0
            for group in q:
                g_val = sum([g.val for g in group])
                g_right_val = total_val - g_val
                for g in group:
                    g.val = g_right_val
                    l,r = g.left,g.right
                    new_group = []
                    if l:
                        new_group.append(l)
                        new_total_val += l.val
                    if r:
                        new_group.append(r)
                        new_total_val += r.val
                    if new_group:
                        t.append(new_group)
            q = t
            total_val = new_total_val
        return root
            
            
