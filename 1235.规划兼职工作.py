#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#
from bisect import bisect_right
# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        将兼职按照endtime升序排列
        动态规划,dp[i]表示前i份工作的最大收益,dp[0]=0。
        dp[i] = max(dp[i-1],dp[k]+profir[i-1])  两种情况，不要第i份工作或者要第i份工作。
        如果要第i份工作，需要找到第k份工作，这个工作的结束时间早于第i份工作的开始时间。即endtime[k-1]<starttimep[i-1]
        """
        work_time = list(zip(startTime,endTime,profit))
        work_time = sorted(work_time,key= lambda x: x[1]) #按照结束时间升序排列
        n = len(startTime)
        dp  = [0] * (n+1)
        for i in range(1,n+1):
            k = bisect_right(work_time,work_time[i-1][0],hi=i,key=lambda x:x[1])
            dp[i] = max(dp[i-1],dp[k]+work_time[i-1][2])
        return dp[-1]
        

# @lc code=end

