#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        if n == 1:
            return 1
        while l<r:
            if r-l < 4:
                for k in range(r-1,l-1,-1):
                    if not isBadVersion(k):
                        return k+1
                return 1
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m

# @lc code=end

