#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    """
    关键点：
    1. 每个单词的长度m都相同。
    2. n个单词的顺序无所谓，但是单词内部不能被截断。
    思路一：
     遍历s中每一段长度为n*m的子串，将其截取为n*m个单词，然后判断是否匹配。（使用集合）
        def findSubstring(self, s: str, words: List[str]) -> List[int]:
            from collections import Counter  #统计每个单词的个数
            if not s or not words: return []
            n = len(words)
            m = len(words[0])
            len_worlds = n*m
            res = []
            words = Counter(words)
            for i in range(len(s)-len_worlds+1):
                tmp = s[i:i+len_worlds]  #截取n*m长度子串
                words_tmp = []
                for j in range(0,len_worlds,m):
                    words_tmp.append(tmp[j:j+m])
                if Counter(words_tmp) == words:
                    res.append(i)
            return res
    思路二：
        承接上面的解法，直接在遍历s时，使用滑动窗口维护所有单词长度总和的队列。
        
    """    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter  #统计每个单词的个数
        if not s or not words: return []
        n = len(words)
        m = len(words[0])
        len_worlds = n*m
        res = []
        words = Counter(words)
        for i in range(len(s)-len_worlds+1):
            tmp = s[i:i+len_worlds]  #截取n*m长度子串
            words_tmp = []
            for j in range(0,len_worlds,m):
                words_tmp.append(tmp[j:j+m])
            if Counter(words_tmp) == words:
                res.append(i)
        return res
# @lc code=end

