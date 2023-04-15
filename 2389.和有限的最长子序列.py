#
# @lc app=leetcode.cn id=2389 lang=python3
#
# [2389] 和有限的最长子序列
#
from typing import List
# @lc code=start
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = list(accumulate(sorted(nums)))
        return [bisect_right(f, q) for q in queries]

# @lc code=end
nums = [736411,184882,914641,37925,214915]
query = [331244,273144,118983,118252,305688,718089,665450]
print(Solution().answerQueries(nums,query))

