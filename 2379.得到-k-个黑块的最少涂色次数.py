#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#
from collections import Counter
# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 滑动窗口
        i,j = 0,k
        res = tmp = Counter(blocks[:k])["W"]
        while j<len(blocks):
            if blocks[j] == "W":
                tmp += 1
            if blocks[i] == "W":
                tmp -= 1
            res = min(res,tmp)
            j += 1
            i += 1
        return res
# @lc code=end

