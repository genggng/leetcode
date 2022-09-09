#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_list = text.split()
        space_len = len(text) - sum([len(word) for word in word_list])
        word_num = len(word_list)
        if word_num == 1:
            return word_list[0] + " "*space_len
        space_inter = space_len // (word_num - 1)
        extra_space = space_len % (word_num - 1)

        # print(space_len,space_inter,word_num)
        return (" "*space_inter).join(word_list) + " "*extra_space

# @lc code=end

