 #
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] 卡车上的最大单元数
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 很简单，贪心算法
        # 选择能够转更多单元的箱子即可
        boxTypes.sort(key=lambda x :x[1],reverse=True)
        res = 0
        for box_num,units in boxTypes:
            num = min(box_num,truckSize)
            res += num*units
            truckSize -= num
            if truckSize == 0:
                break
        return res
# @lc code=end

