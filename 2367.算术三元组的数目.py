#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        len_nums = len(nums)
        res = 0

        seen_set = set()

        for i in range(len_nums-1, -1, -1):
            if nums[i]+diff in seen_set and nums[i]+2*diff in seen_set:
                res += 1
            
            seen_set.add(nums[i])

        
        return res
        
                 



# @lc code=end

