#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt1 = 0
        cnt2 = 0
        vowel = {'a','e','i','o','u','A','E',"I",'O','U'}
        for c in s[:len(s)//2]:
            if c in vowel:
                cnt1 +=1
        for c in s[len(s)//2:]:
            if c in vowel:
                cnt2 += 1
        return bool(cnt1 == cnt2)
# @lc code=end

