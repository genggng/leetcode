#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_col = []
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)
        for i in zero_row:
            for k in range(n):
                matrix[i][k] = 0
        for j in zero_col:
            for k in range(m):
                matrix[k][j] = 0

# @lc code=end

