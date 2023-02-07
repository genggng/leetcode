#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
from typing import List
# @lc code=start
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        """
        当我们已经能够构造[0,x]区间的整数，此时增加一个整数y，我们就能
        构造[0,x]和[y,x+y]区间的整数，如果y<=x，那么就能构造[0,x+y]区间长度
        """
        coins.sort()
        x = 1
        for num in coins:
            if num>x:
                break
            else:
                x += num
        return x
# @lc code=end
x = [1,4,10,3,1]
print(Solution().getMaximumConsecutive(x))
