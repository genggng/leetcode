#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # stack = []
        # for log in logs:
        #     print(log[:2])
        #     if log[:2] == ".." and stack:
        #         stack.pop()
        #     elif log[:2] == "./":
        #         continue
        #     else:
        #         stack.append(log)
        # return len(stack)
        depth = 0
        for log in logs:
            if log == "./":
                continue
            if log != "../":
                depth += 1
            elif depth:
                depth -= 1
        return depth

# @lc code=end

