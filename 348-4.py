from typing import List
"""
6396. 统计整数数目 显示英文描述 
通过的用户数135
尝试过的用户数220
用户总通过次数145
用户总提交次数367
题目难度Hard
给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.
请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。

注意，digit_sum(x) 表示 x 各位数字之和。
"""

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # 剪枝，缩小范围
        
