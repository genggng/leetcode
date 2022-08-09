#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        s = 1
        for num in nums:
            s += num
            if s<1:
                start += (1-s)
                s = 1
        return start
# @lc code=end

