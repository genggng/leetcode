from typing import List

"""
6333. 查询网格图中每一列的宽度 显示英文描述 
给你一个下标从 0 开始的 m x n 整数矩阵 grid 。矩阵中某一列的宽度是这一列数字的最大 字符串长度 。

比方说，如果 grid = [[-10], [3], [12]] ，那么唯一一列的宽度是 3 ，因为 -10 的字符串长度为 3 。
请你返回一个大小为 n 的整数数组 ans ，其中 ans[i] 是第 i 列的宽度。

一个有 len 个数位的整数 x ，如果是非负数，那么 字符串长度 为 len ，否则为 len + 1 。
"""
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        res = [0]*n
        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                res[j] = max(res[j],len(str(num)))
        return res