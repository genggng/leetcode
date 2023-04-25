#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = - 1e5
        cur = 0
        for i,nums in enumerate(nums):
            cur += nums
            res = max(cur,res)
            if cur<0:
                cur = 0
        return res



        




# @lc code=end

