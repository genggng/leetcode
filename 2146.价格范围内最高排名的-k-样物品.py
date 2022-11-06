#
# @lc app=leetcode.cn id=2146 lang=python3
#
# [2146] 价格范围内最高排名的 K 样物品
#

# @lc code=start
from cgitb import reset
from collections import deque
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        """
        广度优先搜索，每一次往外扩散一步。
        同时判断是否搜索够了物品。
        如果当前物品超了，好需要选择本步中优先级更高的哪些物品。
        """
        m = len(grid)
        n = len(grid[0])
        q = deque([(start[0],start[1],0)])
        res = []
        cnt = 0  #当前结果个数
        price = grid[start[0]][start[1]]
        if pricing[0] <= price <= pricing[1]:
            res.append((0,price,start[0],start[1])) #四元组，按级别排序
        grid[start[0]][start[1]] = 0 #已经访问
        old_d = 0
        while q:
            x,y,d = q.popleft() #坐标和距离
            for i,j in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
                if 0<=i<m and 0<=j<n and grid[i][j]>=1:
                    q.append((i,j,d+1))  #下一步能够进行扩散的
                    if pricing[0] <= grid[i][j] <= pricing[1]:
                        res.append((d+1,grid[i][j],i,j))
                        cnt += 1
                    grid[i][j] = 0 #访问过

            if d == old_d + 1: #在每次处理完一个深度时，判断一次数量是否够了
                old_d = d
                if cnt >= k:
                    res.sort()
                    return [x[2:] for x in res[:k]]
        res.sort()
        return [x[2:] for x in res]
            
# @lc code=end
print(Solution().highestRankedKItems([[57,54,48],[652,572,990],[632,199,306],[38,702,263],[431,0,507],[673,570,750],[316,141,639]],[475,745],[3,2],4))

