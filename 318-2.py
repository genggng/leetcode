"""
6230. 长度为 K 子数组中的最大和 显示英文描述 
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        前缀和
        """
        presum = [0]*(len(nums)+1)  #sum[:i]
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]
        # sum[i:i+k] = presum[i+k] - presum[i]
        i,j = 0,k  #子数组[i,j]
        res = 0
        # 用字典和数组来维护非重复数组
        count = dict()
        cnt = 0 #当前子数组中非重复元素个数
        for num in nums[:k]:
            if num not in count.keys():
                cnt += 1
                count[num] = 0
            count[num] += 1
        n = len(nums)
        while True:
            if cnt == k:
                res = max(res,presum[j]-presum[i])
            j += 1
            if j > n:
                break
            if nums[j-1] not in count.keys() or count[nums[j-1]] == 0:
                cnt += 1
                count[nums[j-1]] = 0
            count[nums[j-1]] += 1
            
            if count[nums[i]] == 1:
                cnt -= 1
            count[nums[i]] -= 1
            i += 1
        return res



