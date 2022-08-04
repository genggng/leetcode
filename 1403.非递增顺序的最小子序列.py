#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        half_sum = sum(nums) // 2
        nums.sort(reverse=True)
        s = 0
        res = []
        for x in nums:
            s += x
            res.append(x)
            if s > half_sum:
                break
        return res

# @lc code=end

