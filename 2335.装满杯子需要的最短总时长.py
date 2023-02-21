#
# @lc app=leetcode.cn id=2335 lang=python3
#
# [2335] 装满杯子需要的最短总时长
#

# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        尽量让每杯水都有能配对的。
        假设A最多：
        如果A=B+C 那么刚好完美配对
        如果A>B+C 那么A多余的只能单独接
        如果A<B+C 那么B和C在和A配对后，进行完美配对
        """
        amount.sort(reverse=True)
        A,B,C = amount
        if A >= B+C:
            return A
        if A<B+C:
            return A + math.ceil((B+C-A)/2)
        
# @lc code=end

