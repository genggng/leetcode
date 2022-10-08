#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 递归定义括号字符串
        # 起始：是空字符
        # 递归：如果A,B都是有效字符串，那么AB，也是有效的，
        # （A）也是有效的

        # 求解：左右括号数目相同不就行了吗？XXX
        # 必须是符合括号匹配
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if c == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)  #没有匹配的数量

# @lc code=end
s = "()))(("
print(Solution().minAddToMakeValid(s))
