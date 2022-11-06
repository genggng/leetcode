#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from curses.ascii import isdigit


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def dfs(i,tmp):
            if i == n:
                res.append("".join(tmp))
                return
            tmp.append(s[i])
            dfs(i+1,tmp) #原字符算一类
            tmp.pop()  #复原

            if s[i].islower():
                tmp.append(s[i].upper())
                dfs(i+1,tmp)
                tmp.pop()  #复原

            if s[i].isupper():
                tmp.append(s[i].lower())
                dfs(i+1,tmp)
                tmp.pop()  #复原
        dfs(0,[])
        return res    


# @lc code=end

