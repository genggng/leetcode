#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """
        贪心算法,假设a<b<c
        如果a+b<=c 那么a,b只与c进行匹配，最终答案为a+b
        如果a+b>c 那么a,b只与c进行匹配，并且轮流使用a，b中大者与c匹配。
        待c=0时，再将a,b互相匹配，最终答案为c+ ((a-k1)+(b-k2))/2 = (a+b+c)//2
        """
        v = [a,b,c]
        v.sort()
        if v[0]+v[1]<=v[2]:
            return v[0] + v[1]
        else:
            return sum(v)//2
# @lc code=end

