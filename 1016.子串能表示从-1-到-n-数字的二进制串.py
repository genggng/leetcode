#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#
# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (58.32%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 19.6K
# Testcase Example:  '"0110"\n3'
#
# 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回
# false 。
# 
# 子字符串 是字符串中连续的字符序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "0110", n = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "0110", n = 4
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s[i] 不是 '0' 就是 '1'
# 1 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # 反向，统计s所有子串的二进制值在[1,n]的个数，如果等于n则通过
        seen = set()
        s = list(map(int,s))
        for i,x in enumerate(s):
            if x == 0: continue  #起始位置i如果为0，直接跳过，前导0不影响值。
            j = i+1
            while x<=n:
                seen.add(x)
                if j == len(s):break
                x = (x<<1) | s[j]  # 从子串[i,j]的二进制计算[i,j+1]的二进制
                j += 1
        return len(seen) == n
# @lc code=end

