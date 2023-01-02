#
# @lc app=leetcode.cn id=1801 lang=python3
#
# [1801] 积压订单中的订单总数
#

import heapq
from typing import List
# @lc code=start
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_heap = []
        sell_heap = []
        for order in orders:
            price,amount,ordertype = order
            if ordertype == 0:
                # 这是一个buy订单
                if not sell_heap or sell_heap[0][0] > price:
                    heapq.heappush(buy_heap,(-1*price,amount))
                else:
                    while sell_heap and sell_heap[0][0] <= price:
                        sell_price,sell_amount = heapq.heappop(sell_heap)
                        if sell_amount > amount:
                            heapq.heappush(sell_heap,(sell_price,sell_amount-amount))
                            amount = 0
                            break
                        elif sell_amount == amount:
                            amount = 0
                            break
                        else:
                            amount -= sell_amount
                            continue
                    if amount > 0:
                        heapq.heappush(buy_heap,(-1*price,amount))
            else:
                # 这是一个sell订单
                if not buy_heap or -1*buy_heap[0][0] < price:
                    heapq.heappush(sell_heap,(price,amount))
                else:
                    while buy_heap and -1*buy_heap[0][0] >= price:
                        buy_price,buy_amount = heapq.heappop(buy_heap)
                        if buy_amount > amount:
                            heapq.heappush(buy_heap,(buy_price,buy_amount-amount))
                            amount = 0
                            break
                        elif buy_amount == amount:
                            amount = 0
                            break
                        else:
                            amount -= buy_amount
                            continue
                    if amount > 0:
                        heapq.heappush(sell_heap,(price,amount))
        num1 =  sum(list(zip(*buy_heap))[1]) if buy_heap else 0
        num2 =  sum(list(zip(*sell_heap))[1]) if sell_heap else 0
        return (num1+num2) % int(1e9+7)         
# @lc code=end
x = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
print(Solution().getNumberOfBacklogOrders(x))
