#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
# class Solution:
#     def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
#         pieces = set([str(x) for x in pieces])
#         i = 0
#         while i<len(arr):
#             for j in range(1,len(arr) - i+1):
#                 sub_arr = arr[i:i+j]
#                 if str(sub_arr) in pieces:
#                     i += j
#                     break
#             else:
#                 return False
#         return True

# 优化，按照列表收个元素建立哈希表，因为每个元素出现一次，因此凭借首个元素就能确定列表
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] not in index: #只用比较首元素即可，因为首先要能匹配上首元素
                return False
            p = pieces[index[arr[i]]] #如果首元素能匹配上，那么整个列表就必须匹配上
            if arr[i: i + len(p)] != p:
                return False
            i += len(p)
        return True

# @lc code=end

