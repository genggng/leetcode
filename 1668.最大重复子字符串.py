#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        动态规划，f[i]记录sequence[:i+1]中存在的最大重复度
        """
        n,m = len(sequence),len(word)
        f = [0]*n
        for i in range(m-1,n):
            if sequence[i-m+1:i+1] == word:
                f[i] = (0 if i == m-1 else f[i-m]) +1
        return max(f)
        
# @lc code=end
print(Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))
