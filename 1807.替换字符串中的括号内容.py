#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res = []
        i,j = 0,0
        know_dict = {key:value for key,value in knowledge}
        while j < len(s):
            c = s[j]
            if  c == "(" and i<j:
                res.append(s[i:j])
                i = j
            if c == ")":
                key = s[i+1:j]
                value = know_dict[key] if key in know_dict.keys() else "?"
                res.append(value)
                i = j+1
            j += 1
        if s[-1] != ")":
            res.append(s[i:j])
        return "".join(res)
        
# @lc code=end

