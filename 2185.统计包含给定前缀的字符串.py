#
# @lc app=leetcode.cn id=2185 lang=python3
#
# [2185] 统计包含给定前缀的字符串
#

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) < len(pref):
                continue
            if word[:len(pref)] == pref:
                res += 1
        return res
# @lc code=end

