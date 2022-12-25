"""
6273. 最多可以摧毁的敌人城堡数目 显示英文描述 
题目难度Easy
给你一个长度为 n ，下标从 0 开始的整数数组 forts ，表示一些城堡。forts[i] 可以是 -1 ，0 或者 1 ，其中：

-1 表示第 i 个位置 没有 城堡。
0 表示第 i 个位置有一个 敌人 的城堡。
1 表示第 i 个位置有一个你控制的城堡。
现在，你需要决定，将你的军队从某个你控制的城堡位置 i 移动到一个空的位置 j ，满足：

0 <= i, j <= n - 1
军队经过的位置 只有 敌人的城堡。正式的，对于所有 min(i,j) < k < max(i,j) 的 k ，都满足 forts[k] == 0 。
当军队移动时，所有途中经过的敌人城堡都会被 摧毁 。

请你返回 最多 可以摧毁的敌人城堡数目。如果 无法 移动你的军队，或者没有你控制的城堡，请返回 0 。
"""
from typing import List
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        """
        寻找-1和1之间最长的0
        """
        res = 0
        i =0
        while i < len(forts)-1:
            start = forts[i]
            tmp = 0
            if start == 1 or start == -1:
                for j in range(i+1,len(forts)):
                    if forts[j] == 0:
                        tmp += 1
                    elif forts[j] == -1*(start):
                        res = max(tmp,res)
                        i = j
                        break
                    else:
                        i = j
                        break
                else:
                    i = j
            else:
                i += 1
        return res
print(Solution().captureForts([-1,-1,1,-1,-1,0]))             

