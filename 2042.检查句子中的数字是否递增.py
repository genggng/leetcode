#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split(" ")
        pre = -1
        for token in tokens:
            if token.isdigit():
                if int(token) > pre:
                    pre = int(token)
                else:
                    return False
        return True

# @lc code=end

