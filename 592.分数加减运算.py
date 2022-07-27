#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#

# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        计算所有分母的最小公倍数，然后进行通分计算。
        假设初始的分子son为0，分母mom为1
        我们不断读取下一个分数，与只相加
        son = mom1*son2 + mom2*son1
        mon = mom1*mom2
        """
        son,mom = 0,1
        i,n = 0,len(expression)
        while i<n:
            son1,sign = 0,1
            if expression[i] == "-" or expression[i] == "+":  #获取符号位
                if expression[i] == "-":
                    sign = -1
                i += 1
            while i<n and expression[i].isdigit(): #获取分子
                son1 = son1*10 + int(expression[i])
                i += 1
            son1 = sign*son1  #加上符号位
            i += 1

            mom1 = 0
            while i<n and expression[i].isdigit(): #获取分母
                mom1 = mom1*10 + int(expression[i])
                i += 1
            son = son1*mom + son*mom1
            mom = mom*mom1
        if son == 0:  #分母为0，直接返回
            return "0/1"
        g = gcd(abs(son),mom)  #约分
        return f"{son//g}/{mom//g}"


# @lc code=end

