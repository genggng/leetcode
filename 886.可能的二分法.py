#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
from collections import deque

from pyparsing import col


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 广度优先搜索
        g = [[] for _ in range(n)]
        for x,y in dislikes:  #统计讨厌的人
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        color = [0] * n
        for i,c in enumerate(color):
            if c == 0:  #还没被分配组
                q = deque([i])
                color[i] = 1  #设为红色
                while q:
                    x = q.popleft()
                    for y in g[x]: # x讨厌的人
                        if color[y] == color[x]:  #颜色一样
                            return False
                        if color[y] == 0:  #还没访问到
                            color[y] = -color[x] #设为蓝色
                            q.append(y)
        return True


        

# @lc code=end

