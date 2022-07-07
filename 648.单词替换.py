#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
class Solution:
    """
    哈希集合：用python的集合查找对应的字符串，时间复杂度为O(1)
    总体时间复杂度为O(n*m) n为单词个数，m为单词平均长度 
    """
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_list = sentence.split(" ")
        dictionary_set = set(dictionary)
        for i,words in enumerate(sentence_list):
            for j in range(len(words)):  #从短到长遍历单词，看是否有前缀
                if words[:j+1] in dictionary_set: 
                    sentence_list[i] = words[:j+1]  #找到最短前缀，替换
                    break    
        return " ".join(sentence_list)            
# @lc code=end

