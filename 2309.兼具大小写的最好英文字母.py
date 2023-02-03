#
# @lc app=leetcode.cn id=2309 lang=python3
#
# [2309] 兼具大小写的最好英文字母
#

# @lc code=start
class Solution:
    def greatestLetter(self, s: str) -> str:
        s_dict = set()
        res = '0'  #起始字符
        for c in s:
            if c.isupper() and c.lower() in s_dict or c.islower() and c.upper() in s_dict:
                if c.upper() > res:
                    res = c.upper()
            s_dict.add(c)
        return res if res >'0' else ""

# @lc code=end

