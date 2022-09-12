#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        这是一道智力题：
        当k=1(最小)时,只需要[1,2,3,4,5...,n]即可
        当k=n-1(最大)时，只需要[1,n,2,n-1,3,n-3...]即可
        其他当k=[1,n-1] 只需要将两种进行混合即可
        [1,2,...,n-k,n,n-k+1,n-1,n-k+2,n-2...]
        """
        answer = list(range(1,n-k))
        i,j = n-k,n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i,j = i+1,j-1
        return answer
# @lc code=end

