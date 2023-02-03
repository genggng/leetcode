#
# @lc app=leetcode.cn id=2319 lang=python3
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = grid[i][j]
                if i == j or i == n-1-j:
                    if x == 0:
                        return False
                else:
                    if x != 0:
                        return False
        return  True
# @lc code=end

