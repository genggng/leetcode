#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#

# @lc code=start
from enum import EnumMeta


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        groupsize[i]相同时， i一定在同一个组中。
        """
        group = [(size,index) for index,size in enumerate(groupSizes)]
        group.sort(key=lambda x:x[0])
        res = []
        i = 0
        while i<len(group):
            size = group[i][0]
            tmp = []
            end = i + size
            while i < end:
                tmp.append(group[i][1])
                i += 1
            res.append(tmp)
        return res


# @lc code=end

