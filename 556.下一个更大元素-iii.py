#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        和第31. 下一个排列一致
        """
        nums = list(str(n))
        n = len(nums)
        if n == 1: return -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                right = i+1  
                for j in range(i+1,n):
                    if nums[i]<nums[j]< nums[right]:
                        right = j   #更新较大的数
                nums[i],nums[right] = nums[right],nums[i] #交换两个数
                nums[i+1:] = sorted(nums[i+1:])  #升序排列
                res = int("".join(nums))
                if res > 2**31 -1: return -1
                else: return res
        return -1 
# @lc code=end

