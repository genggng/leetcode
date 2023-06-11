#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#
# https://leetcode.cn/problems/equal-row-and-column-pairs/description/
#
# algorithms
# Medium (71.61%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 23.5K
# Testcase Example:  '[[3,2,1],[1,7,6],[2,7,7]]'
#
# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
# 
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
# 输出：1
# 解释：存在一对相等行列对：
# - (第 2 行，第 1 列)：[2,7,7]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# 输出：3
# 解释：存在三对相等行列对：
# - (第 0 行，第 0 列)：[3,1,2,2]
# - (第 2 行, 第 2 列)：[2,4,2,2]
# - (第 3 行, 第 2 列)：[2,4,2,2]
# 
# 
# 
# 
# 提示：
# 
# 
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 10^5
# 
# 
#
from typing import List
# @lc code=start
import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = {}
        colum_dict = {}
        n = len(grid)
        grid = np.array(grid)
        for i in range(n):
            row = str(grid[i])
            if row not in row_dict.keys():
                row_dict[row] = 0
            row_dict[row] += 1

            colum = str(grid[:,i])
            if colum not in colum_dict.keys():
                colum_dict[colum] = 0
            colum_dict[colum] += 1
        res = 0
        for key in set(row_dict.keys()) & set(colum_dict.keys()):
            res += row_dict[key] * colum_dict[key]
        
        return res
        
# @lc code=end
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(Solution().equalPairs(grid))

