#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#
from typing import List
# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        pre = -1
        for num in nums:
            if num > pre:
                cur += num
            else:
                res = max(cur,res)
                cur = num
            pre = num
        res = max(cur,res)
        return res

# @lc code=end
print(Solution().maxAscendingSum([10,20,30,5,10,50]))
