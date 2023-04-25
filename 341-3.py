from typing import List,Optional

"""
6375. 构造有效字符串的最少插入数 显示英文描述 
给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。

如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效
"""
class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        t = ['a','b','c']
        i = 0
        k = 0
        while k < len(word):
            c = word[k]
            cur_i = t.index(c)
            if cur_i >= i:
                dis = cur_i - i  #要补得单词
                res += dis
                i = (cur_i+1)%3
                k += 1
            else:  #补全
                dis = 3 - i
                res += dis
                i = 0
        else:
            if i != 0:
                dis = 3 - i
                res += dis
                i = 0  
        return res

print(Solution().addMinimum("aaa"))

