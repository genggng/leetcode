#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        min_distance = inf
        for i,(p_x,p_y) in enumerate(points):
            if p_x == x or p_y == y:
                dis = abs(x-p_x) + abs(y-p_y)
                if dis<min_distance:
                    res = i
                    min_distance = dis

        return res
# @lc code=end

