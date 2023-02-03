#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 > sum2:
            nums1,nums2 = nums2,nums1
        diff = abs(sum2-sum1)
        if diff == 0:
            return 0
        nums1 = [6-x for x in nums1]
        nums2 = [x-1 for x in nums2]
        sum_all = nums1 + nums2
        sum_all.sort(reverse=True)
        cnt =0
        for num in sum_all:
            diff -= num
            cnt += 1
            if diff <=0:
                return cnt
        return -1
        # 将两个数组中最大值变小，最小值变大。
# @lc code=end

