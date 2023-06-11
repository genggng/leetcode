from typing import List

"""
6472. 查询后矩阵的和 显示英文描述 
通过的用户数97
尝试过的用户数161
用户总通过次数97
用户总提交次数179
题目难度Medium
给你一个整数 n 和一个下标从 0 开始的 二维数组 queries ，其中 queries[i] = [typei, indexi, vali] 。

一开始，给你一个下标从 0 开始的 n x n 矩阵，所有元素均为 0 。每一个查询，你需要执行以下操作之一：

如果 typei == 0 ，将第 indexi 行的元素全部修改为 vali ，覆盖任何之前的值。
如果 typei == 1 ，将第 indexi 列的元素全部修改为 vali ，覆盖任何之前的值。
请你执行完所有查询以后，返回矩阵中所有整数的和。
"""
import numpy as np
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # 暴力法,超时

        # mat = np.zeros((n,n))
        # for t,i,v in queries:
        #     tmp = [v]*n
        #     if t == 0:
        #         mat[i,:] = tmp
        #     else:
        #         mat[:,i] = tmp
        
        # return mat.sum()
        res = 0
        row_list  = [(0,-1)]*n
        colom_list = [(0,-1)]*n

        # 整个矩阵应该还是稀疏的。
        for idx,(t,i,v) in enumerate(queries):
            if t == 0:
                row_list[i] = (v,idx)
            else:
                colom_list[i] = (v,idx)
        res = 0
        for i in range(n):
            for j in range(n):
                rv,ri = row_list[i]
                cv,ci = colom_list[j]
                v = rv if ri>=ci else cv
                res += v
        return res 

querys = [[1,0,6]]
print(Solution().matrixSumQueries(1,querys))


