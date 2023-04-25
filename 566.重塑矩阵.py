#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        if m*n != r*c:
            return mat
        if m == r and n == c:
            return mat
        # 转成一维数组
        t = []
        for row in mat:
            t += row
        res = []
        i = 0
        while i<len(t):
            res.append(t[i:i+c])
            i += c
        return res
# @lc code=end

