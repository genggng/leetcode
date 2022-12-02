#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 遍历一遍即可
        max_height = 0
        cur_heght = 0
        for g in gain:
            cur_heght += g
            max_height = max(max_height,cur_heght)
        return max_height
# @lc code=end

