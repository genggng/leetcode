#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        判断每个单词是否有其父串。
        """
        res = []
        for word in words:
            for f_word in words:
                if word == f_word: continue
                if word in f_word:
                    res.append(word)
                    break
        return res

# @lc code=end

