from typing import List,Optional

"""
6350. 找出可整除性得分最大的整数 显示英文描述 
给你两个下标从 0 开始的整数数组 nums 和 divisors 。

divisors[i] 的 可整除性得分 等于满足 nums[j] 能被 divisors[i] 整除的下标 j 的数量。

返回 可整除性得分 最大的整数 divisors[i] 。如果有多个整数具有最大得分，则返回数值最小的一个。
"""

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        score = []
        for d in divisors:
            t = 0
            for num in nums:
                if num%d == 0:
                    t += 1
            score.append(t)
        max_score = max(score)
        res = []
        for i,s in enumerate(score):
            if max_score == s:
                res.append(divisors[i])
        return min(res)