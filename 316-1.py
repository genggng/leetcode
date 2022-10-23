"""
6214. 判断两个事件是否存在冲突 显示英文描述 
给你两个字符串数组 event1 和 event2 ，表示发生在同一天的两个闭区间时间段事件，其中：

event1 = [startTime1, endTime1] 且
event2 = [startTime2, endTime2]
事件的时间为有效的 24 小时制且按 HH:MM 格式给出。

当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 冲突 。

如果两个事件之间存在冲突，返回 true ；否则，返回 false 。
"""
from typing import List
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time2min(event):
            mins = []
            for t in event:
                h,m = map(int,t.split(":"))
                mins.append(h*60+m)
            return mins
        start1,end1 = time2min(event1)
        start2,end2 = time2min(event2)
        if end1 < start2 or end2< start1:
            return False
        return True
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]
print(Solution().haveConflict(event1,event2))
