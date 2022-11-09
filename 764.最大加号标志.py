#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#
from typing import List
# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """
        阶数的上限为(n+1)//2，下限为0.
        动态规划 dp[i][j][k]表示the max number of continuous 1以(i,j) as center in direction k(0,1,2,3) 
        则the order from center (i,j) = min(dp[i][j])
        """
        # 暴力法，计算每个以grid[i][j]为中心的阶数。
        mines = set(map(tuple,mines))

        dp = [[n]*n for _ in range(n)]
        # dp = [[n]*n]*n
        # flag = bool(dp == dp1)
        for i in range(n):
            # left
            count = 0  #统计在第i行，(i,j)左边最长连续1个数
            for j in range(n):
                count = 0 if (i,j) in mines else count+1
                dp[i][j] = min(dp[i][j],count)
            
            # right
            count = 0  #统计在第i行，(i,j)右边最长连续1个数
            for j in range(n-1,-1,-1):
                count = 0 if (i,j) in mines else count+1
                dp[i][j] = min(dp[i][j],count)
        for j in range(n):
            # up
            count = 0  #统计在第j列，(i,j)上边最长连续1个数
            for i in range(n):
                count = 0 if (i,j) in mines else count+1
                dp[i][j] = min(dp[i][j],count)
            
            # down
            count = 0  #统计在第j列，(i,j)下边最长连续1个数
            for i in range(n-1,-1,-1):
                count = 0 if (i,j) in mines else count+1
                dp[i][j] = min(dp[i][j],count)
        return max(map(max,dp))    
        # dp = [[n] * n for _ in range(n)]
        # banned = set(map(tuple, mines))
        # for i in range(n):
        #     # left
        #     count = 0
        #     for j in range(n):
        #         count = 0 if (i, j) in banned else count + 1
        #         dp[i][j] = min(dp[i][j], count)
        #     # right
        #     count = 0
        #     for j in range(n - 1, -1, -1):
        #         count = 0 if (i, j) in banned else count + 1
        #         dp[i][j] = min(dp[i][j], count)
        # for j in range(n):
        #     # up
        #     count = 0
        #     for i in range(n):
        #         count = 0 if (i, j) in banned else count + 1
        #         dp[i][j] = min(dp[i][j], count)
        #     # down
        #     count = 0
        #     for i in range(n - 1, -1, -1):
        #         count = 0 if (i, j) in banned else count + 1
        #         dp[i][j] = min(dp[i][j], count)
        # return max(map(max, dp))


# @lc code=end
print(Solution().orderOfLargestPlusSign(5,[[4,2]]))
