#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        逐层计算每一层的酒杯的容量
        """
        row = [poured]
        for i in range(1,query_row + 1):
            nextRow = [0]*(i+1)  #下一行的杯子的容量
            for j,v in enumerate(row): #根据本行每个杯子，计算往下一层流的酒
                if v >1:
                    nextRow[j] += (v-1)/2   #溢出的流向下一层的两杯
                    nextRow[j+1] += (v-1)/2
            row = nextRow  # 更新行
        return min(1,row[query_glass])  #找到第query_row行和第query_class个酒杯

# @lc code=end

