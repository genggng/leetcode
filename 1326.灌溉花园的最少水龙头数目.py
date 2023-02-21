#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#

# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 转化为区间合并问题
        # 使用动态规划解决
        inter = []
        for i,x in enumerate(ranges):
            start = max(0,i-x)
            end = min(n,i+x)
            inter.append((start,end))
        inter.sort()
        
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for start,end in inter:
            if dp[start] == float("inf"):
                return -1 # 存在无法弥补的空隙
            for k in range(start,end+1):
                dp[k] = min(dp[k],dp[start]+1)
        return dp[-1]
# @lc code=end

