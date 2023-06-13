from typing import List

"""
6424. 半有序排列 显示英文描述 
通过的用户数1338
尝试过的用户数1428
用户总通过次数1340
用户总提交次数1553
题目难度Easy
给你一个下标从 0 开始、长度为 n 的整数排列 nums 。

如果排列的第一个数字等于 1 且最后一个数字等于 n ，则称其为 半有序排列 。你可以执行多次下述操作，直到将 nums 变成一个 半有序排列 ：

选择 nums 中相邻的两个元素，然后交换它们。
返回使 nums 变成 半有序排列 所需的最小操作次数。

排列 是一个长度为 n 的整数序列，其中包含从 1 到 n 的每个数字恰好一次。
"""
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        idx_1 = nums.index(1)
        idx_n = nums.index(n)
        res = idx_1 + n - 1 - idx_n
        return res if idx_1<idx_n else res - 1  