#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)  # dp[i] 表示以i结尾的分割最大和
        for i in range(1,n+1):
            maxValue = arr[i-1]
            for j in range(i-1,max(-1,i-k-1),-1):
                maxValue = max(arr[j],maxValue)
                dp[i] = max(dp[i],dp[j] + maxValue*(i-j))
                    
        
        return dp[-1]

# @lc code=end

