#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_value = -1
        second_value = -1
        for x in nums:
            if x > first_value:
                second_value = first_value
                first_value = x

            elif x > second_value:
                second_value = x

        return (first_value-1)*(second_value-1)
# @lc code=end

