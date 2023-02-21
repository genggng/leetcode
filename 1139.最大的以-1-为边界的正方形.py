#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#

from typing import List
# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        import numpy
        # 暴力法，遍历所有size的网格
        n,m = len(grid),len(grid[0])
        grid = numpy.array(grid)
        for size in range(min(n,m),1,-1):
            conv = numpy.zeros((size-2,size-2))
            conv = numpy.pad(conv,pad_width = 1,mode = 'constant',constant_values = 1)
            for i in range(n-size+1):
                for j in range(m-size+1):
                    res = numpy.multiply(grid[i:i+size,j:j+size],conv).sum()
                    if res == (size-1)*4:
                        return size*size
        return 1 if 1 in grid else 0


# @lc code=end
grid = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().largest1BorderedSquare(grid))

