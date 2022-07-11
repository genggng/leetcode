#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#

# @lc code=start
class MagicDictionary:
    """
    使用数组存储所有的单词。
    查询时：
    遍历所有单词，寻找合适的的魔法单词：长度和待查找的相同，并且有且只有一位字母不同。

    """

    def __init__(self):
        self.words = list()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            
            diff = 0
            for chx, chy in zip(word, searchWord):
                if chx != chy:
                    diff += 1
                    if diff > 1:
                        break
            
            if diff == 1:
                return True
        
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

