#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        模拟法，看能否弹出
        """
        stack = []
        i,j = 0,0
        while i<len(pushed) and j <len(popped):
            while i < len(pushed) and (not stack or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1
            while j < len(popped) and (stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
        return bool(not stack)


# @lc code=end

