#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start

from math import factorial


class Solution:
    def __init__(self) -> None:
        # 构建100以内的质数表
        self.table = [2,3,5,7,11,13,17,19]
        for i in range(20,101):
            is_prime = True
            for x in self.table:
                if i % x == 0:
                    is_prime = False
                    break
            if is_prime: self.table.append(i)

    def numPrimeArrangements(self, n: int) -> int:
        """
        题目意思：质数只能和质数交换位置，非质数也是如此。
        统计n内的质数个数
        返回质数全排列*非质数全排列。
        """
        prime_num = 0
        for x in self.table:
            if n>=x: prime_num += 1
        return factorial(prime_num)*factorial(n-prime_num) % int(1e9+7)

# @lc code=end

