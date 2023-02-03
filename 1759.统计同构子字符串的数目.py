#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同构子字符串的数目
#

# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        """
        将相同字符串进行分组即可
        """
        for k, g in groupby(s):
            n = len(list(g))
            res += (n + 1) * n // 2
        return res % (10 ** 9 + 7)

# @lc code=end

