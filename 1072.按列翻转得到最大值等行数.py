#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#
# https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/description/
#
# algorithms
# Medium (62.97%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 15.6K
# Testcase Example:  '[[0,1],[1,1]]'
#
# 给定 m x n 矩阵 matrix 。
# 
# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
# 
# 返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] == 0 或 1
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # 寻找本质相同的行
        m,n = len(matrix),len(matrix[0])
        cnt = []
        for i in range(m):
            line = matrix[i]
            if line[0] == 1:
                for j in range(n):
                    matrix[i][j] = 1^matrix[i][j]
            cnt.append(str(line))
        return max(Counter(cnt).values())

# @lc code=end
mat = [[0,1],[1,0]]
print(Solution().maxEqualRowsAfterFlips(mat))
