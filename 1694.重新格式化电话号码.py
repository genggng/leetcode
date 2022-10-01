#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        s1 = [c for c in number if c.isdigit() ]
        r = len(s1) % 3
        if r == 0:  #需要保留3个数字
            r_num = 3 
        if r == 1: #需要保留4个数字
            r_num = 4
        if r == 2:  #需要保留2个数字
            r_num = 2
        res = []
        i = 0
        while i < len(s1) - r_num:
            res.append("".join(s1[i:i+3]))
            i += 3
        if r_num == 4:
            res.append("".join(s1[i:i+2]))
            res.append("".join(s1[i+2:i+4]))
        else:
            res.append("".join(s1[-1*r_num:]))
        
        return "-".join(res)

# @lc code=end

