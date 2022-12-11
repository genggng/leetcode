#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                res += (nums[i-1]+1 - nums[i])
                nums[i] = nums[i-1] + 1
        return res

# @lc code=end

