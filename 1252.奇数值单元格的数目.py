#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#
from typing import List

# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """
        对于某个单元格，有唯一的坐标（x,y）
        其正负性变化为：其坐标x,y在indices出现次数总和的奇偶性。
        每次加+1相当于正负性翻转。
        """
        x_flip = [0]*m  # x坐标受到的翻转次数
        y_flip = [0]*n  # y坐标受到的翻转次数

        for r,c in indices:
            # print("r,c",r,c)
            x_flip[r] = x_flip[r]^1  #翻转
            y_flip[c] = y_flip[c]^1

        # print(x_flip,y_flip)
        x_flip_count = sum(x_flip)
        y_flip_count = sum(y_flip)

        # 翻转的行*每行元素数+翻转的列*每列元素数 - 翻转两次的交叉部分*2
        # 为什么乘2，一个是因为交叉元素会被计算两次翻转，而是因为翻转两次为偶数
        res = x_flip_count*n + y_flip_count*m - 2*x_flip_count*y_flip_count
        return res
# @lc code=end
print(Solution().oddCells(48,37,[[40,5]]))
