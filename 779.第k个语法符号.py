#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 存在两个基本单元：0(x) 和 1(y)
        # 单元x,y 下一层会产生 01(x+y)和10(y+x)
        # 做法会超时，指数增加
        # x = [0]
        # y = [1]
        # if n <= 2:
        #     return (x+y)[k-1]
        # for i in range(n-2):
        #     x,y = x+y,y+x
        # return (x+y)[k-1]

        """
        其实这题很容易联想到二叉树，从根节点0开始，左子节点不变，右子节点翻转。
        而最深的一层的二进制索引k上的每一个0就表示进入左子节点，每一个1就表示进入右子节点，
        所以只需要计算k二进制表示中1的数量，再检查他的奇偶性就可以了。
        """
        return list(bin(k-1)[2:]).count("1") & 1
        
        
# @lc code=end

