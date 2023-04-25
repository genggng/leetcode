from typing import List
"""
6336. 设计可以求最短路径的图类 显示英文描述 
给你一个有 n 个节点的 有向带权 图，节点编号为 0 到 n - 1 。图中的初始边用数组 edges 表示，其中 edges[i] = [fromi, toi, edgeCosti] 表示从 fromi 到 toi 有一条代价为 edgeCosti 的边。

请你实现一个 Graph 类：

Graph(int n, int[][] edges) 初始化图有 n 个节点，并输入初始边。
addEdge(int[] edge) 向边集中添加一条边，其中 edge = [from, to, edgeCost] 。数据保证添加这条边之前对应的两个节点之间没有有向边。
int shortestPath(int node1, int node2) 返回从节点 node1 到 node2 的路径 最小 代价。如果路径不存在，返回 -1 。一条路径的代价是路径中所有边代价之和。
"""
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[float("inf")]*n for _ in range(n)]
        for src,dest,cost in edges:
            self.graph[src][dest] = cost

    def addEdge(self, edge: List[int]) -> None:
        src,dest,cost = edge
        self.graph[src][dest] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        dis = self.Dijkstra(node1,node2)
        return dis if dis != float("inf") else -1
    
    def Dijkstra(self,start,dest):
    # 输入是从 0 开始，所以起始点减 1
        G = self.graph
        inf = float('inf')
        node_num = len(G)
        # visited 代表哪些顶点加入过
        visited = [0] * node_num
        # 初始顶点到其余顶点的距离
        dis = {node: G[start][node] for node in range(node_num)}
        # parents 代表最终求出最短路径后，每个顶点的上一个顶点是谁，初始化为 -1，代表无上一个顶点
        parents = {node: -1 for node in range(node_num)}
        # 起始点加入进 visited 数组
        visited[start] = 1
        # 最开始的上一个顶点为初始顶点
        last_point = start

        for i in range(node_num - 1):
            # 求出 dis 中未加入 visited 数组的最短距离和顶点
            min_dis = inf
            for j in range(node_num):
                if visited[j] == 0 and dis[j] < min_dis:
                    min_dis = dis[j]
                    # 把该顶点做为下次遍历的上一个顶点
                    last_point = j
            # 最短顶点假加入 visited 数组
            visited[last_point] = 1
            # 对首次循环做特殊处理，不然在首次循环时会没法求出该点的上一个顶点
            if i == 0:
                parents[last_point] = start + 1
            for k in range(node_num):
                if G[last_point][k] < inf and dis[k] > dis[last_point] + G[last_point][k]:
                    # 如果有更短的路径，更新 dis 和 记录 parents
                    dis[k] = dis[last_point] + G[last_point][k]
                    parents[k] = last_point + 1
        return dis[dest]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)