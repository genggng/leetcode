#
# @lc app=leetcode.cn id=2037 lang=python3
#
# [2037] 使每位学生都有座位的最少移动次数
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        # 最小操作：
        # 对当前座位和学生排序
        # 第i个学生去第i个座位。
        return sum([abs(x-y) for x,y in zip(seats,students)])
# @lc code=end

