#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
from curses.ascii import isdigit


class Solution:
    def reformat(self, s: str) -> str:
        res = []
        num_list = []
        letter_list = []
        
        for c in s:
            if c.isdigit():
                num_list.append(c)
            else:
                letter_list.append(c)

        if len(letter_list)>len(num_list):
            while num_list and letter_list:
                res.append(letter_list.pop())
                res.append(num_list.pop())
        else:
            while num_list and letter_list:
                res.append(num_list.pop()) 
                res.append(letter_list.pop())

        if len(num_list) == 1:
            res.append(num_list.pop())
        elif len(letter_list) == 1:
            res.append(letter_list.pop())
        elif len(num_list) == 0 and len(letter_list) == 0:
            pass
        else:
            return ""

        return "".join(res)

# @lc code=end

