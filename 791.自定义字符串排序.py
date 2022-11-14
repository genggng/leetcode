#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_set = set(order)
        c2idx = {c:i for i,c in enumerate(order)}
        s_in_idx = []
        s_out = []
        for c in s:
            if c in order_set:
                s_in_idx.append(c2idx[c])
            else:
                s_out.append(c)
        s_in_idx.sort()
        return "".join([order[i] for i in s_in_idx])+"".join(s_out)
# @lc code=end

