#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        关键点：将后面一个较大的数与前面一个较小的数互换，从而使得整个数最大。

        如何寻找较小的数：从后往前遍历，第一个升序对(i,j),i就是那个数。如果遍历到
    其实也没有找到升序对，说明整个数组都是降序排列的，已经是最大值。
        如何寻找较大的数：找到较大的数后，向后遍历，找到第一个比i大的数k （一定存在，
    至少j就是一个）。
        交换两者后，把高位之后的数字都升序排列，从而获得最小的值。
        """
        n = len(nums)
        if n == 1: return
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                right = i+1  
                for j in range(i+1,n):
                    if nums[i]<nums[j]< nums[right]:
                        right = j   #更新较大的数
                nums[i],nums[right] = nums[right],nums[i] #交换两个数
                nums[i+1:] = sorted(nums[i+1:])  #升序排列
                return 

        nums.sort()       

# @lc code=end

