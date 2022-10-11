#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # s1和s2恰好有两个字符不相同
        count = 0
        words = []
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                words.append((c1,c2))
                count += 1
            if count > 2:
                return False
        if len(words) == 0 or len(words) == 2 and words[0] == words[1][::-1]:
            return True
        return False
            

# @lc code=end

