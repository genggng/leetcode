#
# @lc app=leetcode.cn id=2357 lang=python3
#
# [2357] 使数组中所有元素都等于零
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        add = 0
        res = 0
        for num in nums:
            diff = num-add
            if diff >0:
                res += 1
                add += diff
        return res
# @lc code=end

