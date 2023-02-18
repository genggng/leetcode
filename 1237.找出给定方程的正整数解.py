#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        #  二分查找 x in [1,1000],y in [1,1000]
        # res = []
        # for x in range(1,1001):
        #     y = 1 + bisect_left(range(1,1000),z,key=lambda y:customfunction.f(x,y))
        #     if customfunction.f(x,y) == z:
        #         res.append([x,y])
        # return res
        # 假设f(x,y) == z，那么符合条件的x增大时，y一定缩小。
        res = []
        y = 1000
        for x in range(1,1001):
            while y>0 and customfunction.f(x,y) > z:
                y -= 1
            if y == 0:
                break  # 搜索完毕
            if customfunction.f(x,y) == z:
                res.append([x,y])
        return res
# @lc code=end

