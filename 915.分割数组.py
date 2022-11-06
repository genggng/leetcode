#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # min_value[i] 记录nums[i:]的最小值
        n = len(nums)
        min_value = [0]*n
        min_tmp = 10e7 
        for i in range(n-1,-1,-1):
            min_value[i] = min(min_tmp,nums[i])
            min_tmp = min_value[i]
        max_tmp = -1
        for i in range(n-1):
            max_tmp = max(nums[i],max_tmp)
            if max_tmp <= min_value[i+1]:
                return i+1



# @lc code=end

