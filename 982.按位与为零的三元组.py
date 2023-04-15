#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#

# @lc code=start
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter((x & y) for x in nums for y in nums)
        
        ans = 0
        for x in nums:
            for mask, freq in cnt.items():
                if (x & mask) == 0:
                    ans += freq
        return ans

# @lc code=end

