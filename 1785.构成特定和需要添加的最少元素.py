#
# @lc app=leetcode.cn id=1785 lang=python3
#
# [1785] 构成特定和需要添加的最少元素
#
import math
# @lc code=start
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil((abs(goal-sum(nums)))/limit)
# @lc code=end

