#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#

# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [[False] * n for _ in range(n)]
        degree = [0] * n
        for a, b in roads:
            connect[a][b] = True
            connect[b][a] = True
            degree[a] += 1
            degree[b] += 1

        maxRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - connect[i][j]
                maxRank = max(maxRank, rank)
        return maxRank

# @lc code=end

