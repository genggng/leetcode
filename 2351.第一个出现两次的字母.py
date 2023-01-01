#
# @lc app=leetcode.cn id=2351 lang=python3
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visit = set()
        for c in s:
            if c in visit:
                return c
            visit.add(c)
# @lc code=end

