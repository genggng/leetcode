#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
from collections import Counter
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i,c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
# @lc code=end

