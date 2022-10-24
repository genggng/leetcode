"""
6224. 最大公因数等于 K 的子数组数目 显示英文描述 

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。

子数组 是数组中一个连续的非空序列。

数组的最大公因数 是能整除数组中所有元素的最大整数。
"""
from typing import List
import math
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        """
        判断是否为公因数很简单，取模即可。
        只需再判断是否为最大公因数
        """
        res = 0
        left = 0  #找到一段全是k倍数的区间
        pre_flag = False  #是否前面有公因子
        for i,num in enumerate(nums):
            if num % k == 0: #是因子
                nums[i] = nums[i] // k
                if not pre_flag: 
                    left = i
                    pre_flag=True
            else:
                if pre_flag:
                    # 判断区间[left,i]可能存在的子数组
                    for l in range(left,i):
                        for r in range(l,i):
                            if r == l:
                                g = nums[r]
                            else:
                                g = math.gcd(g,nums[r])
                            if g == 1:
                                res += i-r
                                break
                pre_flag = False
        if pre_flag:
            i += 1
            # 判断区间[left,i]可能存在的子数组
            for l in range(left,i):
                for r in range(l,i):
                    if r == l:
                        g = nums[r]
                    else:
                        g = math.gcd(g,nums[r])
                    if g == 1:
                        res += i-r
                        break
        pre_flag = False

        return res
print(Solution().subarrayGCD([9,3,1,2,6,3],3))