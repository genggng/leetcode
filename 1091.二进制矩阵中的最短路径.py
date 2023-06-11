#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (38.73%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 173.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
# 
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n -
# 1)）的路径，该路径同时满足下述要求：
# 
# 
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 
# 
# 畅通路径的长度 是该路径途经的单元格总数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[0,1],[1,0]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
# 
# 
# 示例 3：
# 
# 
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(0,0)]
        res = float("inf")
        level = 1
        seen = set([])
        while q:
            t = [] 
            for node in q:
                if node not in seen:
                    seen.add(node)
                    if node == (n-1,n-1):
                        res = min(res,level)
                    x,y = node
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            if dy == 0 and dy ==0:
                                continue
                            n_x,n_y = x+dx,y+dy
                            if 0<=n_x<n and 0<=n_y<n and grid[n_x][n_y] == 0:
                                t.append((n_x,n_y))
            level +=1 
            q = t
        
        return res if res != float("inf") else -1
# @lc code=end
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))

