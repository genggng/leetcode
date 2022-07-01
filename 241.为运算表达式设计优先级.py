#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        给表达式加括号，有多少种方式。
        使用分治思想， 对于x op y,最终结果的组合取决于x结果的组合数和y结果的组合数
        c = x op y,将c的加括号方式数转变为x的加括号方式数和y的加括号方式数
        算法流程：
        1. 分解：按照运算符分为两部分，分别求解
        2. 求解：设计递归函数，输入算式，输出算式的解
        3. 合并：根据运算符合并两部分的解，得到最终解
        """
        # 只有数字，直接返回
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i,chr in enumerate(expression):
            if chr in ['+','-','*']:
                # 找到运算符，划分子问题
                left = self.diffWaysToCompute(expression[:i]) #运算符左边的结果列表
                right = self.diffWaysToCompute(expression[i+1:]) #运算右边的结果列表
                for l in left:
                    for r in right:
                        res.append(eval(str(l)+chr+str(r)))  #使用eval表达式编译公式

        return res 
# @lc code=end

