from typing import List,Optional

"""
6376. 一最多的行 显示英文描述 

给你一个大小为 m x n 的二进制矩阵 mat ，请你找出包含最多 1 的行的下标（从 0 开始）以及这一行中 1 的数目。

如果有多行包含最多的 1 ，只需要选择 行下标最小 的那一行。

返回一个由行下标和该行中 1 的数量组成的数组。
"""
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0,0]
        for i,row in enumerate(mat):
            s = sum(row)
            if res[1] < s:
                res[0] = i
                res[1] = s
        return res