#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
from collections import Counter
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2)<k:
            return False
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:k])
        if cnt1 == cnt2:
            return True
        for i in range(len(s2)-k):
            cnt2[s2[i]] -= 1
            cnt2[s2[k+i]] += 1
            if cnt1 == cnt2:
                return True
        return False
    
# @lc code=end
s1 = "ab"
s2 = "eidboaoo"

print(Solution().checkInclusion(s1,s2))
