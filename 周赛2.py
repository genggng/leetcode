"""
6201. 找出前缀异或的原始数组 显示英文描述 

题目难度Medium
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
注意 ^ 表示 按位异或（bitwise-xor）运算。

可以证明答案是 唯一 的。
"""
from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        一步步算
        第一位确定等于pref
        """
        res = [0] * len(pref)
        res[0] = pref[0]
        cur_xor = pref[0]
        for i in range(1,len(pref)):
            pref_num = pref[i]
            x_num = []
            while max(pref_num,cur_xor) > 0:
                end_num = pref_num&1
                x_bit = cur_xor&1
                pref_num = pref_num >> 1
                cur_xor = cur_xor >> 1
                if end_num == 1:
                    x_bit = int(not x_bit)
                x_num.append(str(x_bit))
            if not x_num:
                res[i] = 0
            else:
                res[i] = int("".join(x_num[::-1]),2)
            cur_xor = pref[i]
        return res
print(Solution().findArray([5,2,0,3,1]))