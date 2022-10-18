#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#

# @lc code=start
from functools import cache
from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 数位DP模板
        s = str(n)

        # 返回从i填数字，i前面填的数字集合为mask，能构造出的特殊整数的数目
        # is_limit 表示前面填的数字是否都对应n位上，如果为true，那么当前位最多为int(s[i]),否则最多为9
        # is_num 表示前面是否填了数字（是否跳过），如果为true，那么当前位可以从0开始，否则那么我们可以跳过，或者从1开始。
        @cache
        def f(i:int,is_limit:bool,is_num:bool)->int:
            if i == len(s):
                return int(is_num) #递归的重点，如果所有位数都确定好了，返回一个结果1（但是还要保证至少填过数is_num=True，而不是全跳过）
            res = 0
            if not is_num: #如果前面都跳过了,还可以选择继续跳过
                res = f(i+1,False,False)
            up = s[i] if is_limit else '9' #前面是否有限制

            for d in digits: #该位能选择的数字
                if d>up:
                    break
                res += f(i+1,is_limit and d == up,True)
            return res


        return f(0,True,False) #一开始需要限制起始位的上限



# @lc code=end
print(Solution().atMostNGivenDigitSet(['1','3','5'],100))

