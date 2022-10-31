#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        type_idx = {"type":0,"color":1,"name":2}
        idx = type_idx[ruleKey]
        res = 0
        for i in range(len(items)):
            if items[i][idx] == ruleValue:
                res += 1
        return res
# @lc code=end

