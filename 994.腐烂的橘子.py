#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode.cn/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.06%)
# Likes:    684
# Dislikes: 0
# Total Accepted:    109.6K
# Total Submissions: 214.6K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
# 
# 
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 
# 
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
# 
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] 仅为 0、1 或 2
# 
# 
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = []
        new_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    new_orange += 1
        if new_orange == 0:
            return 0
        time = 1
        while q:
            tmp = []
            for x,y in q:
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                        grid[i][j] = 2
                        new_orange -= 1
                        tmp.append((i,j))
                        if new_orange<=0:
                            return time
            q = tmp
            time += 1
        return -1


# @lc code=end
g = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(g))
