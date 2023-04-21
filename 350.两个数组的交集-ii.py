#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from collections import Counter
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        joint = list(set(cnt1) & set(cnt2))
        res = []
        for num in joint:
            cnt = min(cnt1[num],cnt2[num])
            res += [num]*cnt
        return res
# @lc code=end

