#
# @lc app=leetcode.cn id=2293 lang=python3
#
# [2293] 极大极小游戏
#

# @lc code=start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        """
        4个一组，前两个数求最小值，后两个数求最大值。
        1. 模拟法
        """
        
        while True:
            if len(nums) == 1:
                return nums[0]
            n = len(nums)
            t = []
            for i in range(n//2):
                a,b = nums[2*i:2*(i+1)]
                x = min(a,b) if i%2 == 0 else max(a,b)
                t.append(x)
            nums = t

# @lc code=end

