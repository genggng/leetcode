#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[(i+k)%len(res)] = nums[i]
        for i in range(len(nums)):
            nums[i] = res[i]



# @lc code=end

