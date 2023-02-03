#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for cx,cy,r in queries:
            cnt = 0
            for x,y in points:
                if (x-cx)**2 +(y-cy)**2 <= r**2:
                    cnt += 1
            ans.append(cnt)
        return ans
# @lc code=end

