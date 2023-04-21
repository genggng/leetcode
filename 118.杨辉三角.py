#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            pre_row = res[i-1]
            new_row  = [pre_row[0]]
            for j in range(1,len(pre_row)):
                new_row.append(pre_row[j-1]+pre_row[j])
            new_row.append(pre_row[-1])
            res.append(new_row)
        return res
# @lc code=end

