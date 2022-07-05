#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
# class MyCalendar:
#     """
#     方法一：使用元组列表存储日程
#     直接遍历整个元组列表，判断是否能插入

#     判断区间[s1,e1) 和[s2,e2)没有交集，需要s2>=e1 or s1>=e2
#     """
#     def __init__(self):
#         self.tasks = []

#     def book(self, start: int, end: int) -> bool:
#         for l,r in self.tasks:
#             if start<r and l<end:
#                 return False
#         self.tasks.append((start,end))
#         return True
from sortedcontainers import SortedDict

class MyCalendar:
    """
    方法二：使用排序字典存储日程，能够保证排序结构，同时支持快速插入
    使用二分查找合适的位置降低时间复杂度
    """
    def __init__(self):
        self.tasks = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # bisect_left是找到一个合适的位置插入使得原字典有序
        # all(val < end for val in a[lo:i]) 左侧的都小于end
        # all(val >= end for val in a[i:hi]) 右侧（包含i）的都大于等于end
        i = self.tasks.bisect_left(end)  #寻找大于end的第一个节点 r1>=end
        # if r2<=start <ennd <= r1 即可插入
        if i==0 or self.tasks.items()[i-1][1] <=start:  #寻找前一个区间(l2,r2)，r2<=start
            self.tasks[start] = end
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

