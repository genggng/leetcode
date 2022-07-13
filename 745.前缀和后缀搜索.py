#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#

# @lc code=start
class WordFilter:
    """
    直接暴力哈希表，用空间换时间
    记录下所有单词可能的前缀和后缀
    """
    def __init__(self, words: List[str]):
        self.hashmap = {}
        for i,word in enumerate(words):
            for p in range(len(word)):
                for q in range(len(word)):
                    pref = word[:p+1]
                    suff = word[q:]
                    self.hashmap[(pref,suff)] = i

    def f(self, pref: str, suff: str) -> int:
        return self.hashmap.get((pref,suff),-1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end

