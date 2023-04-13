#
# @lc app=leetcode.cn id=2404 lang=python3
#
# [2404] 出现最频繁的偶数元素
#

# @lc code=start
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt_key = {}
        cnt = Counter(nums)
        for k,v in cnt.items():
            if v not in cnt_key:
                cnt_key[v] = []
            if k%2 == 0:
                cnt_key[v].append(k)
        
        for v in sorted(cnt_key.keys(),reverse=True):
            if cnt_key[v]:
                return min(cnt_key[v])
        return -1
        
# @lc code=end

