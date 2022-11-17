#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 两个子数组的均值一定等于nums的均值，
        # 可以转换为寻找一个数组A，使得sum(A)/len(A) == sum(nums)/len(nums)
        # https://space.bilibili.com/206214

        n = len(nums)
        m = n // 2
        s = sum(nums)
        if all(s * i % n for i in range(1, m + 1)):
            return False

        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for x in dp[i - 1]:
                    curr = x + num
                    if curr * n == s * i:
                        return True
                    dp[i].add(curr)
        return False

# @lc code=end

