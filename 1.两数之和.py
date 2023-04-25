#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for i,num in enumerate(nums):
            if num not in val_idx:
                val_idx[num] = set([])
            val_idx[num].add(i)
        for i,num1 in enumerate(nums):
            num2 =  target - num1
            if num1 != num2:
                if num2 in val_idx:
                    return [i,val_idx[num2].pop()]
            else:
                if len(val_idx[num1]) >= 2:
                    return list(val_idx[num1])[:2]
        
# @lc code=end

