"""
6330. 图中的最短环 显示英文描述 

现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。

返回图中 最短 环的长度。如果不存在环，则返回 -1 。

环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次
"""
from typing import List
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        dist = [[float('inf')] * n for _ in range(n)]
        for u, v in edges:
            dist[u][v] = 1
            dist[v][u] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                if dist[i][j] < float('inf') and dist[j][i]< float('inf'):
                    ans = min(ans, dist[i][j] + dist[j][i])
        return ans if ans != float('inf') else -1
n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
print(Solution().findShortestCycle(n,edges))
