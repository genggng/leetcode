#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
import re
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 使用正则表达式
        pattern = ["[a-z]*"+c for c in list(pattern)]
        pattern.append("[a-z]*")
        pattern = "".join(pattern)  #模式
        res = []
        for query in queries:
            flag = True
            match_idx = re.match(pattern,query)
            if match_idx:
                _,end = match_idx.span()
                flag = bool(end == len(query) or query[end:].islower())
            else:
                flag = False

            res.append(flag)
        
        return res

        
# @lc code=end

