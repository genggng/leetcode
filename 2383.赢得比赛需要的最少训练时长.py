#
# @lc app=leetcode.cn id=2383 lang=python3
#
# [2383] 赢得比赛需要的最少训练时长
#

# @lc code=start
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        ene,exper = initialEnergy,initialExperience
        for eg,ex in zip(energy,experience):
            t1,t2 = max(eg-ene+1,0),max(ex-exper+1,0)
            res += (t1+t2)
            ene += (t1-eg)
            exper += (t2+ex)
        return res
# @lc code=end

