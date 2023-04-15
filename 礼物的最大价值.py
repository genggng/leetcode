"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
"""
from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 动态规划
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        t = 0
        for i in range(m):
            dp[i][0] = t + grid[i][0]
            t = dp[i][0]
        t = 0
        for i in range(n):
            dp[0][i] = t + grid[0][i]
            t = dp[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().maxValue(grid))