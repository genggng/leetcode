#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start



class Solution:
    def baseNeg2(self, n: int) -> str:
        """
        k位能表示的最大整数为，奇数为都为1，偶数位都为0
        1位: 1
        3位: 101
        5位  10101
        """
        max = 1  #寻找覆盖n的最小范围
        while max>0 and max<n:
            max = (max << 2) +1
        # res是刚好大于n的最大数，还要计算和n的差值
        # 对于max来说，想要其减小，要么将奇数位由1变成0，要么将偶数位由0变成1
        # 这其实就是对如果需要降低max的某位，就行翻转其
        # 刚好对应异或操作。
        # 异或就是计算差值
        # print(max)
        return bin(max^max-n)[2:]

        
# @lc code=end
n = 2
print(Solution().baseNeg2(n))
