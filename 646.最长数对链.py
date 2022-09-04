#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key=lambda x: x[1])
        res = 0
        end = float("-inf")
        for x in pairs:
            if x[0] > end:
                end = x[1]
                res += 1
        return res
# @lc code=end

