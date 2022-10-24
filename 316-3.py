"""
6216. 使数组相等的最小开销 显示英文描述 
给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

你可以执行下面操作 任意 次：

将 nums 中 任意 元素增加或者减小 1 。
对第 i 个元素执行一次操作的开销是 cost[i] 。

请你返回使 nums 中所有元素 相等 的 最少 总开销。
"""
from typing import List
import math

from pyparsing import nums
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        z = list(zip(nums,cost))
        z.sort() #按照nums升序排列
        
        # 以第一个数字为基准，计算loss
        # 因为已经升序排列，我们能够很清楚哪些是增加哪些是减少
        pre_base = z[0][0]
        res = sum([(z[i][0]-pre_base)*z[i][1] for i in range(len(nums)) ])
        pre_cost = z[0][1]
        tail_cost = sum(cost) - pre_cost
        
        cur_sum_cost = res
        for i in range(1,len(nums)):
            cur_num,cur_cost = z[i]  #更改为第i个为基准
            loss = (cur_num-pre_base)*(pre_cost - tail_cost) #pre_cost都增加，tail_cos都减少
            cur_sum_cost += loss            
            res = min(res,cur_sum_cost)
            pre_base = cur_num
            pre_cost += cur_cost
            tail_cost -= cur_cost
        return res
print(Solution().minCost([1,3,5,2],[2,3,1,14]))



