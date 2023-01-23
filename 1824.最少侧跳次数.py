#
# @lc app=leetcode.cn id=1824 lang=python3
#
# [1824] 最少侧跳次数
#

# @lc code=start
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        动态规划
        d[i][j]表示到达i点的第j个跑道需要的最小侧跳数
        """
        n = len(obstacles)
        d = [1,0,1]
        for i in range(1,n):
            ob = obstacles[i]-1
            minCnt = float('inf')
            for j in range(3):
                if ob == j:
                    d[j] = float("inf")
                else:
                    minCnt = min(minCnt,d[j])
            for j in range(3):
                if j != ob:
                    d[j] = min(d[j],minCnt+1)
        return min(d)



# @lc code=end

