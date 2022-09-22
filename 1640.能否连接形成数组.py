#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces = set([str(x) for x in pieces])
        i = 0
        while i<len(arr):
            for j in range(1,len(arr) - i+1):
                sub_arr = arr[i:i+j]
                if str(sub_arr) in pieces:
                    i += j
                    break
            else:
                return False
        return True
# @lc code=end

