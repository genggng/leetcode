"""
给你一个大小为 m x n 的整数矩阵 grid 。

按以下形式将矩阵的一部分定义为一个 沙漏 ：
"""

# 只用卷积操作即可
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        kernel = [[1,1,1],[0,1,0],[1,1,1]]
        res = 0
        m,n = len(grid),len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                num = 0
                for i_k in range(3):
                    for j_k in range(3):
                        num += grid[i+i_k][j+j_k] * kernel[i_k][j_k]
                res = max(res,num)
        return res
