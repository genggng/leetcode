#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#
import math
# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        # self.res = 0
        """
        典型的深度有限搜索，每个节点有四种可能
        但是会超时！
        """
        # def dfs(a,b,p):
        #     # 某个回合，a,b所剩的汤量，以及当前选择的概率
        #     if a<=0 or b<=0:
        #         if b > 0: #a先分配完
        #             self.res += p
        #         else:   #b也分配完了
        #             if a<=0:  #a和b同时分配完
        #                 self.res += p*0.5
        #         return
        #     dfs(a-100,b,0.25*p)
        #     dfs(a-75,b-25,0.25*p)
        #     dfs(a-50,b-50,0.25*p)
        #     dfs(a-25,b-75,0.25*p)
        # dfs(n,n,1)
        # return self.res
        """
        先将n除以25，问题转化为更小的数值。
        当i>0,j=0时，dp=0  当i=0,j=0时，dp=0.5  当i=0,j=0时，p=1

        41/41 cases passed (52 ms)
        Your runtime beats 53.26 % of python3 submissions
        Your memory usage beats 84.78 % of python3 submissions (15.7 MB)
        """
        n = math.ceil(n/25)
        if n>=179:  #此时概率为0.999990468596
            return 1
        dp = [[0.0]*(n+1) for _ in range(n+1)]
        dp[0] = [0.5] + [1.0]*n
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = 0.25*(dp[max(0,i-4)][j]+dp[max(0,i-3)][max(0,j-1)]+dp[max(0,i-2)][max(0,j-2)]+dp[max(0,i-1)][max(0,j-3)])
        return dp[n][n]



# @lc code=end
Solution().soupServings(100)
