#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#

# @lc code=start
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        mon_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        mon_pre_days = [0]
        for i in range(len(mon_days)):
            mon_pre_days.append(mon_pre_days[i]+mon_days[i])
        def date2day(s):
            mon,day = s.split("-")
            mon,day = int(mon),int(day)
            return mon_pre_days[mon-1] + day
        alice = [date2day(arriveAlice),date2day(leaveAlice)]
        bob = [date2day(arriveBob),date2day(leaveBob)]
        joint = min(alice[1],bob[1]) -  max(alice[0],bob[0]) + 1
        return joint if joint>0 else 0 
# @lc code=end
print(Solution().countDaysTogether("10-01","10-31","11-01","11-31"))

