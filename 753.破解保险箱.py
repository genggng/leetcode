#
# @lc app=leetcode.cn id=753 lang=python3
#
# [753] 破解保险箱
#

# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        寻找一个最短的串，能够包含所有的全排列。
        比如长度为2，可选元素为{0,1}的全排列有：
        {00} {01} {10} {11}
        而 00110 能够包含所有的全排列。
        """
        seen = set()
        ans = list()
        highest = 10 ** (n - 1)

        def dfs(node: int):
            for x in range(k):
                nei = node * 10 + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei % highest)
                    ans.append(str(x))

        dfs(0)
        return "".join(ans) + "0" * (n - 1)
# @lc code=end

