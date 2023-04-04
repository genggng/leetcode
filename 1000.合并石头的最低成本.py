#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
import heapq
# 我的解法不对，只适合非连续取石头
# class Solution:
#     def mergeStones(self, stones: List[int], k: int) -> int:
#         n = len(stones)
#         if (n-1) % (k-1) != 0:
#             # 每次合并都会减少k-1堆，最终需要剩下1堆
#             return -1
#         res = 0
#         # 尽量把数量少的堆进行合并，这样的消耗最少
#         heapq.heapify(stones)  # 转为堆
#         for i in range((n-1)//(k-1)):
#             select = []
#             for _ in range(k):
#                 select.append(heapq.heappop(stones))
#             cost = sum(select)
#             res += cost
#             heapq.heappush(stones,cost)
#         return res

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        d = [[inf] * n for _ in range(n)]
        sum = [0] * n
        s = 0
        for i in range(n):
            d[i][i] = 0
            s += stones[i]
            sum[i] = s

        for L in range(2, n + 1):
            for l in range(n - L + 1):
                r = l + L - 1
                for p in range(l, r, k - 1):
                    d[l][r] = min(d[l][r], d[l][p] + d[p + 1][r])
                if (r - l) % (k - 1) == 0:
                    d[l][r] += (sum[r] - (0 if l == 0 else sum[l - 1]))
        return d[0][n - 1]

# @lc code=end

