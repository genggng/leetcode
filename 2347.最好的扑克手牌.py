#
# @lc app=leetcode.cn id=2347 lang=python3
#
# [2347] 最好的扑克手牌
#
from typing import List
# @lc code=start
from collections import Counter
import numpy as np
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        cnt = np.array(list(Counter(ranks).values()))

        if any(cnt>=3):
            return "Three of a Kind"
        if  any(cnt>=2):
            return "Pair"
        if all(cnt == 1):
            return "High Card"

# @lc code=end
ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
print(Solution().bestHand(ranks,suits))
