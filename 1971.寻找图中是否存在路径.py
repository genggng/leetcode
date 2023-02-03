#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        广度优先搜索，扩散寻找。
        """
        if n == 1:
            return True
        q = deque([source])
        visit = {source} #记录访问的节点
        
        edge_map = {i:[]for i in range(n)}
        for u,v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        while q:
            node = q.popleft()
            arrive_nodes = edge_map[node]
            for arrive_node in arrive_nodes:
                if arrive_node == destination:
                    return True
                if arrive_node not in visit:
                    q.append(arrive_node)
                    visit.add(arrive_node)
        return False


# @lc code=end
print(Solution().validPath(3,[[0,1],[1,2],[2,0]],0,2))
