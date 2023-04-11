#
# @lc app=leetcode.cn id=2399 lang=python3
#
# [2399] 检查相同字母间的距离
#

# @lc code=start
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_idx = {}
        for i,c in enumerate(s):
            if c in first_idx:
                dis = i - first_idx[c]
                if distance[ord(c) - ord('a')] != dis-1:
                    return False
            else:
                first_idx[c] = i
        return True
# @lc code=end

