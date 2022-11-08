#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        使用栈来维护递归过程。

        75/75 cases passed (56 ms)
        Your runtime beats 76.79 % of python3 submissions
        Your memory usage beats 73.21 % of python3 submissions (15.1 MB)
        """
        op_stack = []
        sign_stack = []
        ops = ['!','&','|']
        for c in expression:
            if c in ops:
                op_stack.append(c)  #op入栈
                continue
            if c == ')':  #一个操作结束
                op = op_stack.pop()  #弹出最近一次运算的op
                if op == "!":  #只有操作数
                    num = sign_stack.pop()
                    sign_stack.pop() #弹出'('
                    sign_stack.append('f' if num == 't' else 't')
                else:
                    num_list = []
                    while sign_stack[-1] != "(":
                        num_list.append(sign_stack.pop())
                    sign_stack.pop() #弹出"("
                    if op == "&":
                        sign_stack.append('f' if 'f' in num_list else 't') #与运算
                    else:
                        sign_stack.append('t' if 't' in num_list else 'f') #或运算
            else:
                sign_stack.append(c)
        return True if sign_stack[-1] == 't' else False
            
# @lc code=end
print(Solution().parseBoolExpr("!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))"))

