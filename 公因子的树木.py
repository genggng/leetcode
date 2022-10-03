"""
给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
"""
import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # 构建质数表,只1000以内的即可
        primes = list(filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,1000+1)))
        a_set = set()
        a_dict = {}
        b_set = set()
        b_dict = {}
        for n in primes:
            if a%n == 0:
                a_set.add(n)
                a_dict[n] = 0 
                while a%n == 0:
                    a_dict[n] += 1
                    a = a//n
            if b%n == 0:
                b_set.add(n)
                b_dict[n] = 0
                while b%n == 0:
                    b_dict[n] += 1
                    b = b//n
            if a == 1 or b == 1:
                break
        com_set =  a_set & b_set
        res_dict = {}
        res = 1
        for n in com_set:
            count = min(a_dict[n],b_dict[n])
            res = res*(count+1)
        return res         
            
print(Solution().commonFactors(885,885))

# import math
# def func_get_prime(n):
#   return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,n+1))
# print(list(func_get_prime(32)))