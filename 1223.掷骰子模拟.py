#
# @lc app=leetcode.cn id=1223 lang=python3
#
# [1223] 掷骰子模拟
#

# @lc code=start
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0]*(rollMax[i]) for i in range(6)] for _ in range(n)]

        for j in range(6):
            dp[0][j][0] = 1

        for i in range(1, n):
            for j in range(6):
                for k in range(rollMax[j]):
                    for p in range(6):
                        if p != j:
                            dp[i][p][0] += dp[i-1][j][k]
                            dp[i][p][0] = dp[i][p][0]%1000000007
                        else:
                            if k < rollMax[j]-1:
                                dp[i][p][k+1] += dp[i-1][j][k]
                                dp[i][p][k+1] = dp[i][p][k+1]%1000000007

        ans = 0
        for i in range(6):
            ans += sum(dp[-1][i])
        return ans%1000000007

# @lc code=end

