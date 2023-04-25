from typing import List
"""
6334. 一个数组所有前缀的分数 显示英文描述 
定义一个数组 arr 的 转换数组 conver 为：

conver[i] = arr[i] + max(arr[0..i])，其中 max(arr[0..i]) 是满足 0 <= j <= i 的所有 arr[j] 中的最大值。
定义一个数组 arr 的 分数 为 arr 转换数组中所有元素的和。

给你一个下标从 0 开始长度为 n 的整数数组 nums ，请你返回一个长度为 n 的数组 ans ，其中 ans[i]是前缀 nums[0..i] 的分数。
"""
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        max_value = 0
        sum_score = 0
        for num in nums:
            max_value = max(max_value,num)
            conver_value = num + max_value
            sum_score += conver_value
            res.append(sum_score)
        return res