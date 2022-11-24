#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        认真审题！
        记录最近的大于right的元素位置l
        记录最近的在范围的元素位置r
        那么以i为右端点，符合条件的子数组有 r-l个
        """
        res = 0
        l = r = -1
        for i,num in enumerate(nums):
            if num>right:
                l = i
                r = -1
            if left<=num<=right:
                r = i
            if r != -1:
                res += r - l
        return res

            

        
# @lc code=end

