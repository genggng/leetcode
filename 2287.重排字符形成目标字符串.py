#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#
from collections import Counter
# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        """
        每个字符只能用一次，只需统计target各字符出现次数即可。
        """
        s_dict = Counter(list(s))
        t_dict = Counter(list(target))
        t = []
        for key in t_dict.keys():
            t.append(s_dict[key] // t_dict[key])
        return min(t)
# @lc code=end

