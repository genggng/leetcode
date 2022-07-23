"""
给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。

例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
"""
class Graph:
    def __init__(self, n_vertices):
        self._n_vertices = n_vertices
        self._adj = [[] for _ in range(n_vertices)]
        self.indegrees = [0 for _ in range(n_vertices)] #记录入度

    def add_edge(self, s, t):
        self._adj[s].append(t)
        self.indegrees[t] += 1
    def del_edge(self,s,t):
        self.indegrees[t] -= 1 #减少入度
    def del_node(self,node):
        for t in self._adj[node]:
            self.del_edge(node,t)
        self.indegrees[node] = -1 #删除节点 
class Solution:

    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        """
        所有的子序列构成一个有向无环图DAG
        关键就是看该DAG的拓扑排序是否唯一。
        拓扑排序：不断删除入度为0节点和其射出的边，然后将该节点加入列表。
        如果在排序时，存在多个入度为0的节点，说明排序顺序不唯一，即超序列不唯一。
        """
        shortest_sequence = []
        n = len(nums)
        G = Graph(n)
        for sub_graph in sequences:
            for i in range(len(sub_graph)-1):
                G.add_edge(sub_graph[i]-1,sub_graph[i+1]-1)
        while G.indegrees.count(0) == 1:
            shortest_sequence.append(G.indegrees.index(0)+1)
            G.del_node(shortest_sequence[-1]-1)  #选出的排序数组
        if G.indegrees.count(0) > 1:
            return False
        else:
            return bool(n == len(shortest_sequence))
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for sequence in sequences:
            for x, y in pairwise(sequence):
                g[x - 1].append(y - 1)
                inDeg[y - 1] += 1

        q = deque([i for i, d in enumerate(inDeg) if d == 0])
        while q:
            if len(q) > 1:
                return False
            x = q.popleft()
            for y in g[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return True
