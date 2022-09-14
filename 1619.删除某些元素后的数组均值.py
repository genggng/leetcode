#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        return mean(arr[n//20:n - n //20])
# @lc code=end

