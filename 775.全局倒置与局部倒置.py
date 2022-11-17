#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        全局倒置：任意两个元素i<j，nums[i]>nums[j]，降序对
        局部倒置：相邻两个元素i,i+1,nums[i]>nums[i+1],相邻倒置
        1. nums中是[0,n-1]一个排列
        """
        # 对于每个元素i，在i之后只存在一个元素i+1比其小。
        # 换句话说，对于元素i，最多只可能i+1比其小，i+1之后的元素都要大于等于i
        n = len(nums)
        # 1. 会超时，可以优化
        # for i in range(len(nums)-1):
        #     min_value = min(nums[i+2:]) if i < n-2 else float("inf")
        #     if nums[i] > min_value:
        #         return False
        # return True

        # 2. 优化到O(n)但是还要跑两边，超过25% ,继续优化    
        # min_value = [float("inf")] * (n+1)
        # for i in range(n-1,-1,-1):
        #     min_value[i] = min(nums[i],min_value[i+1])
        # for i in range(len(nums)-1):
        #     if nums[i] > min_value[i+2]:
        #         return False
        # return True
        
        # 3. 只用跑一边
        # 226/226 cases passed (132 ms)
        # Your runtime beats 52.27 % of python3 submissions
        # Your memory usage beats 69.32 % of python3 submissions (25.1 MB)
        min_value = nums[-1]
        for i in range(n-2,0,-1):
            if nums[i-1] > min_value:
                return False
            min_value = min(min_value,nums[i])
        return True

        
# @lc code=end

