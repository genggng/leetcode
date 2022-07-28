#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return arr
        sort_arr = sorted(arr)
        map = {}
        pre_num = sort_arr[0]
        i = 1
        map[pre_num] = i
        for num in sort_arr[1:]:
            if num != pre_num:
                i += 1
            map[num] = i
            pre_num = num
        for i in range(len(arr)):
            arr[i] = map[arr[i]]

        return arr        
# @lc code=end

