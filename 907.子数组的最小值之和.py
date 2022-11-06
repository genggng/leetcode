#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
         1. 暴力法
         遍历所有子串
         时间复杂度O(n^2)
         会超时！！
        """
        # res = 0
        # mod = int(1e9 + 7)
        # n = len(arr)
        # for i in range(n):
        #     min_value = int(1e5)
        #     for j in range(i,n):
        #         min_value = min(min_value,arr[j])
        #         res = (res + min_value)%mod
        # return res

        """
        针对每个元素，寻找其作为最小元素的最长区间（左边界和右边界）
        那么
        """
        MOD = 10 ** 9 + 7
        n = len(arr)
        monoStack = []
        dp = [0] * n
        ans = 0
        for i, x in enumerate(arr):
            while monoStack and arr[monoStack[-1]] > x:
                monoStack.pop()
            k = i - monoStack[-1] if monoStack else i + 1
            dp[i] = k * x + (dp[i - k] if monoStack else 0)
            ans = (ans + dp[i]) % MOD
            monoStack.append(i)
        return ans

# @lc code=end

