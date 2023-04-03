#
# @lc app=leetcode.cn id=2395 lang=python3
#
# [2395] 和相等的子数组
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cur_set = set()
        for i in range(len(nums)-1):
            add = nums[i]+nums[i+1]
            if add in cur_set:
                return True
            else:
                cur_set.add(add)
        return False
# @lc code=end

