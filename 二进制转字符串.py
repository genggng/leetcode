"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。
如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。
"""

class Solution:
    def printBin(self, num: float) -> str:
        # 判断二级制20位即可达到精度
        res = []
        i = 0
        while abs(num-0.0) >= 0.0001 and i < 7:
            num = num*2
            int_n = int(num)
            res.append(str(int_n))
            num = num - int_n
            i += 1
        if i >= 7:
            return "ERROR"
        return "0."+"".join(res)
n = 0.1
print(Solution().printBin(n))