#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#

# @lc code=start
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0]*n
        adj = [[]for _ in range(n)]
        # 先给每个节点涂色为0
        # 然后逐次便利节点，找到与他相临的节点不同的一个颜色，然后染色。
        for i in range(len(paths)):
            x,y = paths[i]
            x,y = x-1,y-1
            adj[x].append(y)
            adj[y].append(x)
        for i in range(n):
            all_color = set([1,2,3,4])
            for y in adj[i]:
                if res[y] in all_color:
                    all_color.remove(res[y])
            res[i] = all_color.pop()
        return res

        
# @lc code=end

