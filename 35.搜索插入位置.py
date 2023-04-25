#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        if target <= nums[0]:
            return 0
        if target > nums[r]:
            return r+1
        while l<r:
            if r-l == 1:
                return r
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m




# @lc code=end

