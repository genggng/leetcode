#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        贪心算法：
        每遇到一个X，就把这个X之后的三个字符都变成o
        这样对子问题一定是最佳的选择。
        """
        res = 0
        i = 0
        while i <len(s):
            if s[i] == "X":
                res += 1
                i += 3
            else:
                i += 1
        return res
# @lc code=end

