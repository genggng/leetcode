#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#

# @lc code=start
import numpy as np
from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]
        grid = np.array(grid)
        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = int(grid[i:i+3,j:j+3].max())
        return res
# @lc code=end
x = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(Solution().largestLocal(x))

