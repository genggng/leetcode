#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#
import math
# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = s = 0
        for i, x in enumerate(nums):
            s += x if i % 2 else -x
        for i, x in enumerate(nums):
            s -= x if i % 2 else -x
            ans += s == 0
            s -= x if i % 2 else -x
        return ans
# @lc code=end

