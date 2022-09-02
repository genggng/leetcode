#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        定义深度有限搜索dfs(node)，返回从该节点出发的最长有向同值路径。
        这个返回值就等于从左子树和从右子树出发的最大值。
        在遍历的过程中，我们计算经过该节点的最长路径= dfs(left) + 1 + dfs(right) + 1 (假设左右子树都和根节点相同)
        """
        ans = 0
        def dfs(node):
            if not node:
                # 空节点，从此出发的有向路径只能为0
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # 计算从根节点向左右树延伸的两个有向同值路径的长度
            left1 = left +1 if node.left and node.val == node.left.val else 0
            right1 = right + 1 if node.right and node.val == node.right.val else 0
            nonlocal ans
            ans = max(ans,left1+right1) #计算经过node节点的最长路径，更新ans
            return max(left1,right1) # 返回的是从node出发的最长有同值向路径
        dfs(root)
        return ans
        

# @lc code=end

