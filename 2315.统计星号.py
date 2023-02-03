#
# @lc app=leetcode.cn id=2315 lang=python3
#
# [2315] 统计星号
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        res = 0
        for c in s:
            if c == "|":
                flag =  not flag
            if not flag and c == "*":
                res += 1
        return res
# @lc code=end

