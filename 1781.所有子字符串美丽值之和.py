#
# @lc app=leetcode.cn id=1781 lang=python3
#
# [1781] 所有子字符串美丽值之和
#

# @lc code=start
from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        """
        暴力求解，遍历所有子字符串
        """
        res = 0
        for i in range(len(s)):
            cnt = Counter()
            mx = 0
            for j in range(i,len(s)):
                cnt[s[j]] += 1
                mx = max(mx,cnt[s[j]])
                res += mx - min(cnt.values())
        return res
# @lc code=end

