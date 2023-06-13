#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#
# https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/description/
#
# algorithms
# Medium (43.23%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 28.1K
# Testcase Example:  '"ababa"'
#
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
# 
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "ababa"
# 输出：3
# 
# 
# 示例 2：
# 
# 输入：text = "aaabaaa"
# 输出：6
# 
# 
# 示例 3：
# 
# 输入：text = "aaabbaaa"
# 输出：4
# 
# 
# 示例 4：
# 
# 输入：text = "aaaaa"
# 输出：5
# 
# 
# 示例 5：
# 
# 输入：text = "abcdef"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。
# 
# 
#

# @lc code=start
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        res = 0
        for i in range(len(text)):
            # step1: 找出当前连续的一段 [i, j)
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1

            # step2: 如果这一段长度小于该字符出现的总数，并且前面或后面有空位，则使用 cur_cnt + 1 更新答案
            cur_cnt = j - i
            if cur_cnt < count[text[i]] and (j < len(text) or i > 0):
                res = max(res, cur_cnt + 1)

            # step3: 找到这一段后面与之相隔一个不同字符的另一段 [j + 1, k)，如果不存在则 k = j + 1
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            res = max(res, min(k - i, count[text[i]]))
            i = j
        return res


# @lc code=end

