#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
from email.policy import default


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        使用动态规划，关键是确定如何表示状态以及状态的转移
        dp[i][j] 表示以a[i],a[j]为结束的子序列的最大长度,i<j
        初始化： dp[i][j] = 2
        转移矩阵： dp[i][j] = max(dp[k][i]+1) (where A[k] + A[i] == A[j])

        但是不优化的方法一会超时，时间复杂度O(n^3)
        """
        # n = len(arr)
        # res = 0
        # dp = [[2 if i<j else 0 for j in range(n)]for i in range(n)]
        # for i in range(1,n):
        #     for j in range(i+1,n):  #j>i
        #         for k in range(i):
        #             if arr[k] + arr[i] == arr[j]:
        #                 dp[i][j] = max(dp[i][j],dp[k][i]+1)
        #                 break # 因为k是严格递增的。只可能存在一个k
        #         res = max(dp[i][j],res)
        # return res if res>2 else 0

        """
        优化过程，用空间换时间。
        使用哈希表，获得value->index的映射。
        这样就能直接找到合适的arr[k]，时间复杂度降到O(n^2)
        """
        n = len(arr)
        res = 0
        dp = [[2 if i<j else 0 for j in range(n)]for i in range(n)]
        k_map = {arr[i]:i for i in range(n)}

        for i in range(1,n):
            for j in range(i+1,n):  #j>i
                k_value = arr[j] - arr[i]  #a[k]+a[i] == a[j]
                k = k_map.get(k_value,-1)
                if 0 <= k < i:
                    dp[i][j] = max(dp[i][j],dp[k][i]+1)

                res = max(dp[i][j],res)
        return res if res>2 else 0

# @lc code=end

