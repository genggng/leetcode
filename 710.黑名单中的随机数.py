#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
from random import randint, random


class Solution:
    """
    直接构造一个去除黑名单的列表，随机返回列表元素
    会超时
    def __init__(self, n: int, blacklist: List[int]):
        self.random_list = set(range(n))
        self.random_list = list(self.random_list - set(blacklist))
        self.index = random

    def pick(self) -> int:
        return choice(self.random_list)
    """
    def __init__(self, n: int, blacklist: List[int]):
        # 使用哈希表，将[0,n-m-1]的黑名单数字映射到[n-m,n-1]白名单。这样只用在[0,n-m-1]取随机数即可
        self.b2w = {}
        m = len(blacklist)
        self.bound = n-m-1  #能够取到的最大数字
        w = self.bound+1  #被映射的白名单起始
        black = {b for b in blacklist if b>self.bound} #在范围外的黑名单数字
        for b in blacklist:
            if b<=self.bound:  #在范围内的黑名单数字，需要映射
                while w in black:  #w已经在黑名单，需要找个白名单的
                    w += 1
                self.b2w[b] = w
                w += 1
    def pick(self) -> int:
        x = randint(0,self.bound)
        return self.b2w.get(x,x)  #不在映射表，就直接返回x

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

