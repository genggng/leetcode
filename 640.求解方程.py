#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
from curses.ascii import isdigit


class Solution:
    def solveEquation(self, equation: str) -> str:
        num_sum = 0
        coff_sum  = 0
        flag = 1
        sign = 1
        num = 0
        firo_zero = True  # 默认是系数为1
        for c in equation:
            if c.isdigit():
                num  = num*10 + int(c)
                firo_zero = False  #存在数字可能是系数0
            else:
                if c == "x":
                    if num == 0 and firo_zero:
                        num = 1
                    coff_sum += flag*sign*num
                    sign = 1
                else:
                    num_sum += flag*sign*num
                    if c == "+":
                        sign = 1
                    elif c == "-":
                        sign = -1
                    elif c == "=":
                        flag = -1
                        sign = 1
                    else:
                        pass
                firo_zero = True  #更新标志位
                # print(num_sum,coff_sum)
                num = 0
        if equation[-1].isdigit():
            num_sum += flag*sign*num

        if coff_sum == 0:
            if num_sum == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return f"x={-1*num_sum // coff_sum}"

# @lc code=end

