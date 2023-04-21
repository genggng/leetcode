#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
from collections import Counter
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for key in cnt1.keys():
            if key not in cnt2 or cnt1[key] > cnt2[key]:
                return False
        return True 

# @lc code=end

