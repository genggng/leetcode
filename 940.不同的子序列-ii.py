#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = 1  # 空字符串
        mod = int(1e9 + 7)
        preCount = [0]*26  # 记录每个字上次作为结尾的子序列个数
        for c in s:
            add = dp  # 新增的以字母c为结尾的子序列个数
            dp = ((dp + add) % mod - preCount[ord(c)-ord('a')] + mod) % mod  # 负数要加上再取模
            preCount[ord(c)-ord('a')] = add  # 下次字母c再出现，当做重复项减去
        return dp - 1 #减去空串
# @lc code=end

