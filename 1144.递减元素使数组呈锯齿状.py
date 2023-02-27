#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#

# @lc code=start
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        # 分情况模拟
        # 1. 偶数索引大于奇数索引，因为只能减而不能加，因此固定偶数项不动，减奇数项
        res1 = 0
        res2 = 0
        n = len(nums)
        for i in range(n):
            if i%2 == 1:
                l,r = nums[i-1],nums[i+1] if i<n-1 else 99999
                res1 += max(nums[i] - min(l,r)+1,0)
            if i%2 == 0:
                l,r = nums[i-1] if i>0 else 99999,nums[i+1] if i<n-1 else 99999
                res2 += max(nums[i] - min(l,r)+1,0)
        return min(res1,res2)

# @lc code=end

