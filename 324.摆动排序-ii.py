#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        关键点：
        小数和大数交错出现。
        解法：
        将原数组排序，分成两段。把后一段的大数间隔地插入小数中间。
        [1,2,3,4,5,6]->[1,2,3],[4,5,6]->[1,4,2,5,3,6]

        但是无法解决重复数字问题
        最多有(len(nums)+1)//2个重复数字，否则无解。
        [1,2,3,3,3,4]->[1,3,2,3,3,4] #error!
        注意重复数字在小数的末端和大数的前端，因此我们可以将两个数组逆序。
        这样合并时就不会出现相邻的情况。
        [1,2,3,3,3,4]->[3,2,1],[4,3,3]->[3,4,2,3,1,3]

        """
        n = len(nums)
        nums.sort()  #要使用原地排序
        min_nums = nums[:(n+1)//2][::-1]
        max_nums = nums[(n+1)//2:][::-1]
        # print(min_nums,max_nums)
        for i in range(n//2):
            nums[2*i] = min_nums[i]
            nums[2*i+1] = max_nums[i]
        if n&1: #奇数
            nums[-1] = min_nums[-1]

# @lc code=end

