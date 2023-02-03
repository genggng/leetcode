#
# @lc app=leetcode.cn id=1780 lang=python3
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        转换为3进制，并且每一位要么为0，要么为1。
        """
        while n>0:
            r = n%3
            n = n//3
            if r>1:
                return False
        return True

# @lc code=end

