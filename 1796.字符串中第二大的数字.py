#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        t = []
        for c in s:
            if c.isdigit():
                t.append(c)
        t = list(set(t))
        t.sort()
        if len(t)<2 or t[-1] == t[-2]:
            return -1
        else:
            return int(t[-2])
# @lc code=end

