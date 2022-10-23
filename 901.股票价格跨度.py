#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner:
    """
    单调栈
    """
    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        cur_idx = 0 if not self.st else self.st[-1][0]+1
        while self.st and price >= self.st[-1][1]:
            self.st.pop()
        
        
        pre_idx = self.st[-1][0] if self.st else -1
        self.st.append((cur_idx,price))
        return cur_idx-pre_idx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

