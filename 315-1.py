"""
给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。

返回正整数 k ，如果不存在这样的整数，返回 -1 。

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0

"""
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos_set = set()
        neg_set = set()
        res = -1
        for num in nums:
            if num > 0:
                if -1*num in neg_set:
                    res = max(res,num)
                pos_set.add(num)
            if num < 0:
                if -1*num in pos_set:
                    res = max(res,-1*num)
                neg_set.add(num)
        return res
print(Solution().findMaxK(nums=[-1,10,6,7,-7,1]))