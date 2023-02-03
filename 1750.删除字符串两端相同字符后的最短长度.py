#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        i,j = 0,len(s)-1
        while i<j:
            c1 = s[i]
            c2 = s[j]
            if c1!=c2:
                break
            while i<=j and s[i] == c1:
                i += 1
            while i<=j and s[j] == c2:
                j -= 1
        return max(j-i+1,0)

# @lc code=end
# s = "cabaabac"
s = "bbbbbbbbbbbbbbbbbbb"
print(Solution().minimumLength(s))
