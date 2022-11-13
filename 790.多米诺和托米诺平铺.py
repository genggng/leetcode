#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        """
        找规律，归纳法。
        f(1) = 1 f(2) = 2 f(3) = 5
        f(i) = 2*f(i-x) +f(i-3)
        """
        x1,x2,x3 = 1,2,5
        for _ in range(n-3):
            x4 = 2*x3 + x1
            x1,x2 = x2,x3
            x3 = x4
        return [1,2,5][n-1] if n <=3 else x3 % int(1e9 + 7)
# @lc code=end

