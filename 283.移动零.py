#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # t = []
        # for num in nums:
        #     if num != 0:
        #         t.append(num)
        # for i in range(len(t)):
        #     nums[i] = t[i]
        # for i in range(len(t),len(nums)):
        #     nums[i] = 0
        n = len(nums)
        l,r = 0,0 #l指向处理好序列的结尾，r指向非零元素

        while r<n:
            if nums[r] !=0:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            r += 1


# @lc code=end

