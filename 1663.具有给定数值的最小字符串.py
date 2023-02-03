#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        求各位和为k的n位数的最小数字。
        """
        r = k - n  #需要增加的数值
        # 每一位最高增加25位。
        res = []
        while r > 0:
            if r >= 25:
                res.append('z')
            else:
                res.append(chr(ord('a')+r))
                break
            r -= 25
        res += ["a"]*(n-len(res))
        return "".join(res[::-1])

# @lc code=end

