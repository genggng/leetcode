#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        首先统计出所有只有一个元素的行和列
        然后确定这些行列的焦点是否为1
        """
        res = 0
        row_num = [0]* len(mat)
        col_num = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_num[i] += 1
                    col_num[j] += 1
        for i in range(len(mat)):
            if row_num[i] == 1:
                for j in range(len(mat[0])):
                    if col_num[j] == 1 and mat[i][j] == 1:
                        res += 1
                        break
        return res
# @lc code=end

