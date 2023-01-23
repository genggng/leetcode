#
# @lc app=leetcode.cn id=2303 lang=python3
#
# [2303] 计算应缴税款总额
#

# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        last_upper = 0
        res = 0
        for upper,percent in brackets:
            res += (min(upper,income) - last_upper)*percent/100
            if income <= upper:
                break
            last_upper = upper
        return res
# @lc code=end

