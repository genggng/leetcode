#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = []
        i,j = 0,0
        while i<m and j<n:
            a1,a2 = nums1[i],nums2[j]
            if a1<=a2:
                t.append(a1)
                i += 1
            else:
                t.append(a2)
                j += 1
        for k in range(i,m):
            t.append(nums1[k])
        for k in range(j,n):
            t.append(nums2[k])
        for k in range(m+n):
            nums1[k] = t[k]
# @lc code=end

