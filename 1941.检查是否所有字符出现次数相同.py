#
# @lc app=leetcode.cn id=1941 lang=python3
#
# [1941] 检查是否所有字符出现次数相同
#

# @lc code=start
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(list(s))
        values = [value for value in count.values()]
        return len(set(values)) == 1
# @lc code=end

