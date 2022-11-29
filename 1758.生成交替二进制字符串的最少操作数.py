#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        #交替字符串只有两种形式，要么1开始，要么0开始
        #计算每种情况的分数即可
        n = len(s)
        cnt1 = 0
        cnt2 = 0
        c1,c2 = "1","0"
        for i,c in enumerate(s):
            cnt1 += 1 if c1 != c else 0
            cnt2 += 1 if c2 != c else 0
            c1,c2 = c2,c1
        return min(cnt1,cnt2)
# @lc code=end

