#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        t = [c if c.isdigit() else " " for c in word]
        num_list = "".join(t).strip().split()
        num_list = map(int,num_list)
        return len(set(num_list))
# @lc code=end

print(Solution().numDifferentIntegers("a123bc34d8ef34"))
