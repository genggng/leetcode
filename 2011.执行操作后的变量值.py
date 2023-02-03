#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if op[0] == "+" or op[-1] == "+":
                res += 1
            else:
                res -= 1
        return res
# @lc code=end

