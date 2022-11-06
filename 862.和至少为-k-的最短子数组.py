#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#

# @lc code=start
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        暴力法：直接遍历所有的子数组
        会超时。
        剪枝1:起始位负值的l直接跳过，是负贡献

        """
        # n = len(nums)
        # res = float("inf")
        # for l in range(n):
        #     if nums[l] < 0:
        #         continue
        #     total = 0
        #     for r in range(l,n):
        #         total += nums[r]
        #         if total >= k:
        #             res = min(res,r-l+1)
        #             break
        # if res == float("inf"):
        #     res = -1
        # return res
        """
        前缀和：preSumArr[i] 即从前i个元素的和
        那么sum[i+1,j+1]=preSumArr[j] - preSumArr[i]
        """
        preSumArr = [0]
        res = len(nums) + 1
        for num in nums:
            preSumArr.append(preSumArr[-1]+num)
        q = deque()
        """
        遍历前缀和数组，q中存储子数组的起始位置。
        当前前缀和（结束位置）需要遍历每一个起始位置,如果符合条件，需要将左端删除。
        因为该左端的最近右端只能是当前前缀和。
        同时，如果q中前缀和大于当前前缀和，那需要将其删除。
        这是因为当前元素更小，并且索引更靠右，一定是更符合条件的左端。
        """
        for i,r_sum in enumerate(preSumArr):
            while q and r_sum - preSumArr[q[0]] >= k:
                res = min(res,i-q.popleft()) #左端出栈
            while q and r_sum <= preSumArr[q[-1]]:
                q.pop() #删除不占优势的左端
            q.append(i) #当前前缀和入栈，作为新的左端
        return res if res<len(nums) + 1 else -1


# @lc code=end

