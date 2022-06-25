class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        解法1：深度优先搜索
        但是会超时
        """
        n = len(costs)
        min_cost = inf
        def dfs(i,j,cur_cost):
            # 剪枝
            nonlocal min_cost
            cur_cost += costs[i][j]
            if cur_cost>=min_cost: return  #直接返回
            if i == n-1:
                if cur_cost<min_cost:
                    min_cost = cur_cost
                    return
            
            # 递归回溯
            dfs(i+1,(j+1)%3,cur_cost)
            dfs(i+1,(j-1)%3,cur_cost)
        dfs(0,0,0)
        dfs(0,1,0)
        dfs(0,2,0)
        return min_cost
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        动态规划
        dp[i][j]表示从0号到i号房子，第i号房子粉刷为j时的最小花费。
        容易知道dp[0][j] = costs[0][j]
        dp[i][j] = min(dp[i-1][j-1]%3,dp[i-1][j+1]%3)+costs[i][j]  i-1房间和i颜色不同
        容易看出dp和consts大小相同，可以使用滚动数组节省空间。
        时间复杂度O(n) 空间复杂度O(1)
        """
        dp = costs[0]
        for i in range(1,len(costs)):
            dp = [min(dp[j-1],dp[j-2])+cost for j,cost in enumerate(costs[i])]
        return min(dp)

