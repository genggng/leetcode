#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Medium (68.24%)
# Likes:    1067
# Dislikes: 0
# Total Accepted:    336.4K
# Total Submissions: 492.9K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 
# 
# 示例 2:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果p和q在同一颗子树，说明还不是祖先。
        # 如过p和q在两颗子树，说明找到了祖先。
        if root.val == p.val or root.val == q.val:
            return root
        pv,qv = p.val,q.val
        if pv>qv:
            pv,qv = qv,pv
        if pv < root.val < qv:
            return root
        if pv > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if qv<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
# @lc code=end

