#
# @lc app=leetcode.cn id=809 lang=python3
#
# [809] 情感丰富的文字
#
from typing import List
# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        """
        对于s中,所有连续出现大于等于3的字母组，我们认为它是被扩展的。
        """
        res = 0
        for word in words:
            i=j=0
            falg = True
            while i < len(s) and j <len(word):
                if s[i] != word[j]:
                    falg = False
                    break
                ch = s[i]
                cnti = 0
                while i <len(s) and s[i] == ch:
                    cnti += 1 #s中相同元素的连续长度
                    i += 1
                cntj = 0
                while j <len(word) and word[j] == ch:
                    cntj += 1
                    j += 1
                if cnti<cntj: #扩张元素应该要比被扩张元素长
                    falg = False
                    break
                if cnti != cntj and cnti < 3: #无法扩张
                    falg = False
                    break
            if i == len(s) and j == len(word) and falg:
                res += 1
        return res


# @lc code=end
Solution().expressiveWords("heeellooo",["hello","hi","helo"])
