"""
给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：

x 的置位数和 num2 相同，且
x XOR num1 的值 最小
注意 XOR 是按位异或运算。

返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

整数的 置位数 是其二进制表示中 1 的数目。
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_b = list(bin(num1)[2:])
        num2_b = list(bin(num2)[2:])
        count_1 = num1_b.count('1')
        count_2 = num2_b.count('1')
        # count_2['0'] = num2_b.count('0') #0是无数的
        if count_2 == count_1: return num1
        if count_2 < count_1:
            for i,c in enumerate(num1_b):
                if c == '1': count_2 -= 1
                if count_2 == 0:
                    return int("".join(num1_b[:i+1])+"0"*(len(num1_b)-i-1),2)
        if count_2 > count_1:
            count_2 = count_2 - count_1
            # 找到存在0的地方，改为1
            for i in range(len(num1_b)-1,-1,-1):
                if num1_b[i] == '0':
                    num1_b[i] = '1'
                    count_2 -= 1
                if count_2 == 0:
                    break
                    # return int("".join(num1_b,2))
            return int("1"*count_2+"".join(num1_b),2)
print(Solution().minimizeXor(1,12))
                