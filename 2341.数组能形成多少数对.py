#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt = 0
        i = 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                cnt += 1
                i += 1
            i += 1
        return [cnt,len(nums)-cnt*2]

# @lc code=end

