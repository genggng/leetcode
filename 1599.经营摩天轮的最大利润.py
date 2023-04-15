#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#
from typing import List
# @lc code=start
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # 模拟法，能上就上，能下就下，计算每个时间节点的最大净利润
        if boardingCost*4<=runningCost:
            return -1
        res = 0
        res_cnt = 0
        cur_profit = 0
        cur_num = 0 # 当前地面的游客
        cnt = 0
        for num in customers:
            cur_num += num
            cnt += 1
            part_num = min(4,cur_num)
            cur_num -= part_num
            cur_profit += part_num*boardingCost - runningCost
            if cur_profit>res:
                res = cur_profit
                res_cnt = cnt
        if cur_num>0:
            add_cnt = cur_num // 4
            cur_profit +=  add_cnt * 4 * boardingCost - add_cnt*runningCost
            cnt += add_cnt
            if cur_profit>res:
                res = cur_profit
                res_cnt = cnt
            cur_profit += (cur_num%4)*boardingCost - runningCost
            if cur_profit>res:
                res = cur_profit
                res_cnt = cnt + 1
        return res_cnt if res>0 else -1 
# @lc code=end
x = [8,3]
b = 5
r = 6
print(Solution().minOperationsMaxProfit(x,b,r))

