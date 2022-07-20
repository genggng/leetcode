#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    # def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    #     """
    #     模拟法，照着做就行。
    #     时间复杂度O(m*n)
    #     空间复杂度O(1)
    #     """
    #     n = len(grid)
    #     m = len(grid[0])
    #     for _ in range(k):
    #         # print(f"m,n={m,n}")
    #         last_num = grid[n-1][m-1]  #最后一个元素
    #         for i in range(n):
    #             tmp = last_num
    #             last_num = grid[i][m-1]  #保存最后一个数字
    #             for j in range(m-1,0,-1):
    #                 grid[i][j] = grid[i][j-1]
    #             grid[i][0] = tmp
    #     return grid
    """
    将二维转为一维处理
    """
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                index1 = (i * n + j + k) % (m * n)
                ans[index1 // n][index1 % n] = v
        return ans


# @lc code=end

