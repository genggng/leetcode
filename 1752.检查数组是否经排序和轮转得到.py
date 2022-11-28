#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        很简单，就是判断该数组能否轮转为有序非严格递增数组。
        需要满足：
        1. 最多只允许递减一次
        2. 如果出现一次递减，那么nums[-1] <= nums[0]
        """
        flag = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag += 1
                if flag > 1:
                    return False
        if flag == 1 and nums[0] < nums[-1]:
            return False
        return True
            
            
        
# @lc code=end

