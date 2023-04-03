#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_list = [x for x,y in points]
        x_list.sort()
        res = 0
        for i in range(len(x_list)-1):
            width = x_list[i+1] - x_list[i]
            if width>res:
                res = width
        return res
# @lc code=end

