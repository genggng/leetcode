#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c2idx = dict()
        res = -1
        for i,c in enumerate(s):
            if c in c2idx.keys():
                res = max(res,i-1-c2idx[c])
            else:
                c2idx[c] = i
        
        return res

# @lc code=end

