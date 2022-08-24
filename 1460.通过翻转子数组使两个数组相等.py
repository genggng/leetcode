#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        可以交换任意两个相邻元素
        因此可以将任意元素移到首位。
        因此就可以匹配第一位。
        递归实现，只需要匹配剩下N-1位就行。

        因此只用保证两者元素数量相同即可。
        """
        return bool(Counter(target) == Counter(arr))
# @lc code=end

