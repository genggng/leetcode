#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        因为是环形，存在两条去目的地的路径
        只需从start沿着环路跑一圈即可。
        用destination将路径分成两半，比较两者大小。
        """
        foward_distance = 0
        back_distance = 0
        n = len(distance)
        is_back = False
        for i in range(n):
            if is_back:
                back_distance += distance[(start+i)%n]
            else:
                foward_distance += distance[(start+i)%n]
                if (start+i+1)%n == destination:
                    is_back = True
        return min(foward_distance,back_distance)

# @lc code=end

