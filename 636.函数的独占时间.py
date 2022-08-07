#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        使用栈模拟函数调用
        """
        res = [0]*n
        func_stack = []
        for log in logs:
            log = log.split(":")
            id,type,timestamp = int(log[0]),log[1],int(log[2])
            if type == "start":
                if func_stack:
                    res[func_stack[-1][0]] += timestamp-func_stack[-1][1]
                    func_stack[-1][1] = timestamp
                func_stack.append([id,timestamp])
            else:
                i,t = func_stack.pop()
                res[i] += timestamp - t +1
                if func_stack:
                    func_stack[-1][1] = timestamp +1
        return res
# @lc code=end

