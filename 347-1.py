from typing import List
"""
6457. 移除字符串中的尾随零 显示英文描述 
通过的用户数1582
尝试过的用户数1634
用户总通过次数1587
用户总提交次数1707
题目难度Easy
给你一个用字符串表示的正整数 num ，请你以字符串形式返回不含尾随零的整数 num 。

 

示例 1：

输入：num = "51230100"
输出："512301"
解释：整数 "51230100" 有 2 个尾随零，移除并返回整数 "512301" 。
示例 2：

输入：num = "123"
输出："123"
解释：整数 "123" 不含尾随零，返回整数 "123" 。
"""
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        new = []
        falg = True
        for c in num[::-1]:
            if falg:
                if c == "0":
                    continue
                else:
                    new.append(c)
                    falg = False
            else:
                new.append(c)
        return int("".join(new[::-1]))
