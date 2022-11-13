from typing import List
"""
6238. 统计构造好字符串的方案数 显示英文描述 
题目难度Medium
给你整数 zero ，one ，low 和 high ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：

将 '0' 在字符串末尾添加 zero  次。
将 '1' 在字符串末尾添加 one 次。
以上操作可以执行任意次。

如果通过以上过程得到一个 长度 在 low 和 high 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。

请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 109 + 7 取余 后返回。
"""
import math
from scipy.special import comb, perm
class Solution:
    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    #     """
    #     每次操作有两种选择，添加0或者1.
    #     那么执行n次操作，就有2^n种可能。
    #     假设zero和one中最大者位max_value,较小者为min_value
    #     每条路径的字符串长度在[n*min_value,n*max_value]
    #     """
    #     # 寻找n1<=n2<=n3<=n4，其中在n1到n4有解，n2到n3的所有可能有一定成立。
    #     max_cnt,min_cnt = max(zero,one),min(zero,one)
    #     n1 = low // max_cnt  #有解
    #     n4 = math.ceil(high / min_cnt) #最大解
    #     res = 0
    #     for n in range(n1,n4+1):
    #         s_len_min,s_len_max = n*min_cnt,n*max_cnt
    #         if s_len_min>=low and s_len_max<=high:
    #             res += 2**n  #第n次操作都可以
    #         else:
    #             # 找到上界和下界剔除的元素数。
    #             add_big_num = max(math.ceil((low - s_len_min)/(max_cnt-min_cnt)),0) # 要增加的大元素个数
    #             del_big_num = max(math.ceil((s_len_max-high)/(max_cnt-min_cnt)),0) # 要删除的大元素个数
    #             # 大元素的个数范围为
    #             cnt = 2**n
    #             if add_big_num > 0:
    #                 for big_num in range(add_big_num):
    #                     cnt -= int(comb(n,big_num))
    #             if del_big_num > 0:
    #                 for big_num in range(del_big_num):
    #                     cnt -= int(comb(n,big_num))
    #             res += cnt
    #     return int(res % int(1e9+7))
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = [0] * (high + 1)
        ans[0] = 1
        # 动态规划，长度为n的字符串的个数。
        for i in range(1, high + 1):
            if i >= zero:
                ans[i] += ans[i - zero] #可以由长度为i-zero的字符串添加zero
            if i >= one:
                ans[i] += ans[i - one] #可以由长度为i-one的字符串添加one
            ans[i] %= 10 ** 9 + 7
        return sum(ans[low:]) % (10 ** 9 + 7)
print(Solution().countGoodStrings(200,200,10,1))


