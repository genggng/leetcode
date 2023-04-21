#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        
        return " ".join([word[::-1] for word in s_list])
# @lc code=end

