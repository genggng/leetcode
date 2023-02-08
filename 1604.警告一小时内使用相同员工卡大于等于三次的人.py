#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#
from typing import List
# @lc code=start
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        daka_dict = {}
        for name,time in zip(keyName,keyTime):
            if name not in daka_dict.keys():
                daka_dict[name] = []
            daka_dict[name].append(time)
        res = set()
        for name,time_list in daka_dict.items():
            if len(time_list)<3:
                continue

            for i,t in enumerate(time_list):
                h,m = map(int,t.split(":"))
                time_list[i] = h*60+m
            time_list.sort()
            for i in range(len(time_list)-2):
                if time_list[i+2] - time_list[i] <= 60:
                    res.add(name)
                    break
        return sorted(list(res))

            

# @lc code=end
name = ["daniel","daniel","daniel","luis","luis","luis","luis"]
time = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
print(Solution().alertNames(name,time))