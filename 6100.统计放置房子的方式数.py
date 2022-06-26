"""
一条街道上共有 n * 2 个 地块 ，街道的两侧各有 n 个地块。每一边的地块都按从 1 到 n 编号。每个地块上都可以放置一所房子。

现要求街道同一侧不能存在两所房子相邻的情况，请你计算并返回放置房屋的方式数目。由于答案可能很大，需要对 109 + 7 取余后再返回。

注意，如果一所房子放置在这条街某一侧上的第 i 个地块，不影响在另一侧的第 i 个地块放置房子。

1 <= n <= 104
大数过不了 8672。
"""
from curses.ascii import SO
import math
class Solution:

    def countHousePlacements(self, n: int) -> int:
        """
        解决思想：插空法
        有n个位置，不相邻最多有(n+1)//2个房子放置
        对于放置i个房子，那么就有n-i个位置是空地。
        使用插空法，在n-i个空地旁边插房子，共有n-i+1个位置
        从里面选择i个位置放房子，共有C(i,n-i+1)种

        """
        res = 1
        tmp = 1
        for i in range(1,(n+1)//2+1):
            # tmp = comb(n-i+1,i)  #这个方法能过，但是超时
            tmp = tmp*(n-2*i+3)*(n-2*i+2)//((n-i+2)*i)  #改为递推，用整除。
            # tmp *=(n-2*i+3)*(n-2*i+2)/((n-i+2)*i) #不能采用这种方法，会产生小数误差
            res += tmp
        
        res = int(res)  
        c = 1e9+7
        return (res*res)%int(c)
s = Solution()
s.countHousePlacements(3)