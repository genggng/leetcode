#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#

# @lc code=start
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        limit, s = list(map(int, str(N + 1))), set()
        n, res = len(limit), sum(9 * perm(9, i) for i in range(len(limit) - 1))
        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, n - i - 1)
            if x in s: 
                break
            s.add(x)
        return N - res
# @lc code=end

