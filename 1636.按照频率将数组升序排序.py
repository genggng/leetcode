#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#

# @lc code=start
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        count = Counter(nums)
        nums.sort(key=lambda x:count[x])
        return nums
# @lc code=end

