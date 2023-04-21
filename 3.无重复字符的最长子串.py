#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        n = len(s)
        res = 0
        seen = set([])
        while r<n:
            while r<n and s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                res = max(res,r-l)
                r += 1

            if r >= n:
                break
            
            while s[l] != s[r-1]:
                seen.remove(s[l])
                l += 1
            else:
                l += 1
        return res
            
# @lc code=end
print(Solution().lengthOfLongestSubstring("abcabcbb"))
