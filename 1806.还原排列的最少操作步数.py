#
# @lc app=leetcode.cn id=1806 lang=python3
#
# [1806] 还原排列的最少操作步数
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        """
        每一次操作：
        1. 将原数据偶数位放在数组前半范围
        2. 奇数位放在数组后半范围
        """
        res = 0
        org = [i for i in range(n)]

        perm = [i for i in range(n)]
        arr = [0 for i in range(n)]
        while True:
            for i in range(n):
                if i%2 == 0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n//2 + (i-1)//2]
            res += 1
            perm = arr.copy()
            if perm == org:
                return res

# @lc code=end
s = Solution()
for i in range(1,20):
    print(i*2,s.reinitializePermutation(i*2))
