#
# @lc app=leetcode.cn id=2363 lang=python3
#
# [2363] 合并相似的物品
#

# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = dict()
        for value,weight in items1:
            if value not in res.keys():
                res[value] = 0
            res[value] += weight
        for value,weight in items2:
            if value not in res.keys():
                res[value] = 0
            res[value] += weight
        res = [[value,weight]for value,weight in res.items()]
        res.sort()
        return res
# @lc code=end

