"""
给你一个长度为 n 的整数数组 nums 。

考虑 nums 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。

换句话说，令 k 是 nums 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 k 的子数组。
返回满足要求的 最长 子数组的长度。

数组的按位与就是对数组中的所有数字进行按位与运算。

子数组 是数组中的一个连续元素序列。

"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 任意两个数字的与操作结果，肯定小于任意一个数字
        # 因此这个子数组的最大的k就是数组中最大的值
        # 只需要保证数组中最大值的个数即可
        # 统计出k连续出现的最大次数
        max_value = max(nums)
        res = cnt = 0
        for num in nums:
            if num == max_value:
                cnt += 1
                res = max(res,cnt)
            else:
                cnt = 0

        return res

nums = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]
print(Solution().longestSubarray(nums))