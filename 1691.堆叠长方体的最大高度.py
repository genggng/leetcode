#
# @lc app=leetcode.cn id=1691 lang=python3
#
# [1691] 堆叠长方体的最大高度
#

# @lc code=start
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        def check(a: List[int], b: List[int]) -> bool:
            return a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]

        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(key=sum)

        @cache
        def dfs(top: int, index: int) -> int:
            if index == n:
                return 0
            height = dfs(top, index + 1)
            if top == -1 or check(cuboids[top], cuboids[index]):
                height = max(height, cuboids[index][2] + dfs(index, index + 1))
            return height
        return dfs(-1, 0)
# @lc code=end

