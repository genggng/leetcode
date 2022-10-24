#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        """
        res = []
        n = min(len(word1),len(word2))
        for c1,c2 in zip(word1[:n],word2[:n]):
            res.append(c1)
            res.append(c2)
        if len(word1) > n:
            res.append(word1[n:])
        if len(word2) > n:
            res.append(word2[n:])
        return "".join(res)
# @lc code=end

