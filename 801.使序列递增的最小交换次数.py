#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#

# @lc code=start
from cmath import inf


class Solution:
    # def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
    #     swap_dp = [inf]*len(nums1)   #在该位置上交换的代价
    #     not_swap_dp = [inf]*len(nums1)   #在该位置上不交换的代价
    #     swap_dp[0] = 1
    #     not_swap_dp[0] = 0
        
    #     #这一题的关键是，该位置换不换只和它前面以及后面的数字有关，离得更远的数字无关。
    #     # 对于两位来说，交换上一位和交换下一位的效果时一样的。
    #     for i in range(1,len(nums1)):
    #         # 比较两种方案的最小值
    #         # 下面代码的含义：
    #         # 可以不交换时： 本位和上位都交换；本文和上位都不叫唤
    #         # 可以交换时： 本文交换，上位不交换；上位交换，本位不交换。
    #         # 当两个if只满足一个时，就是两种情形：必须不交换；必须交换。
    #         # 当两个if都满足时，就是第三种情形： 可交换也可不交换。
    #         # 使用min函数获得三种情形的最小解。
            
    #         if nums1[i]>nums1[i-1] and nums2[i] > nums2[i-1]: #可以不交换
    #             swap_dp[i] = min(swap_dp[i],swap_dp[i-1] + 1)      #交换
    #             not_swap_dp[i] = min(not_swap_dp[i], not_swap_dp[i-1])  #或者不交换

    #         if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]: # 可以交换
    #             swap_dp[i] =  min(swap_dp[i],not_swap_dp[i-1] + 1)   #本位交换
    #             not_swap_dp[i] = min(not_swap_dp[i], swap_dp[i-1])       #上一位交换
        
    #     return min(swap_dp[-1],not_swap_dp[-1])
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a,b = 0,1
        for i in range(1,n):
            at,bt = a,b
            a=b=n
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                a = min(a,at)
                b = min(b,bt+1)
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                a = min(a,bt)
                b = min(b,at+1)
        return min(a,b)
# @lc code=end

"""
动态规划，但是会存在某位交换与否都行，因此需要两个状态
设置两个状态:swqp_df[n]和not_swap_df[n]
"""