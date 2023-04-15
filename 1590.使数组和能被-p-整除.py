#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#

# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0:
            return 0
        y = 0
        index = {0: -1}
        ans = len(nums)
        for i, v in enumerate(nums):
            y = (y + v) % p
            if (y - x) % p in index:
                ans = min(ans, i - index[(y - x) % p])
            index[y] = i
        return ans if ans < len(nums) else -1
# @lc code=end

