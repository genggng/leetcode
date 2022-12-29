#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#
from collections import Counter
# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all_nums = [nums1,nums2,nums3]
        nums_list = []
        for nums in all_nums:
            nums_list += list(set(nums))
        cnt = Counter(nums_list)
        return [key for key,val in cnt.items() if val>1]
# @lc code=end

