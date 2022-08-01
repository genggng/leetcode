#
# @lc app=leetcode.cn id=1374 lang=python3
#
# [1374] 生成每种字符都是奇数个的字符串
#

# @lc code=start
class Solution:
    def generateTheString(self, n: int) -> str:
        if  n&1:  #如果n是个奇数
            return "a"*n
        else:
            return "a"*(n-1)+"b"
# @lc code=end

