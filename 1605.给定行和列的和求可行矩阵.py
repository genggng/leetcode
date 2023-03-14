#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t = min(rowSum[i],colSum[j])
                res[i][j] = t
                rowSum[i] -= t
                colSum[j] -= t
        return res            
# @lc code=end

