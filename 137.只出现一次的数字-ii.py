#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                res.add(num)
            else:
                if num in res:
                    res.remove(num)
        return res.pop()



# @lc code=end

