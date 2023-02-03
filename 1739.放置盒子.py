#
# @lc app=leetcode.cn id=1739 lang=python3
#
# [1739] 放置盒子
#

# @lc code=start
class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        正确的做法是，找到一个墙角，将地面的盒子贴近墙摆放。

        """
        x = int((6 * n) ** (1 / 3))
        ans = x * (x + 1) // 2
        max_n = x * (x + 1) * (x + 2) // 6
        if max_n > n:
            max_n -= ans
            ans -= x
        return ans + ceil((-1 + (1 + 8 * (n - max_n)) ** 0.5) / 2)
# @lc code=end

