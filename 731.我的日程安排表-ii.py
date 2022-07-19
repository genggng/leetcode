#
# @lc app=leetcode.cn id=731 lang=python3
#
# [731] 我的日程安排表 II
#

# @lc code=start
from sortedcontainers import SortedDict
class MyCalendarTwo:
    """
    这道题相较于I，容许二重日程的存在，而不允许三重日程。
    只需要将二重日程标记为I中的普通日程即可使用相同的算法。
    """

    def __init__(self):
        self.tasks = SortedDict()
        self.is_merge = dict() #标记是否是二重

    def book(self, start: int, end: int) -> bool:
        # bisect_left是找到一个合适的位置插入使得原字典有序
        # all(val < end for val in a[lo:i]) 左侧的都小于end
        # all(val >= end for val in a[i:hi]) 右侧（包含i）的都大于等于end
        i = self.tasks.bisect_left(end)  #寻找大于end的第一个节点 end<=l2
        # print(f"task{self.tasks.items()} add ({start,end}) find i={i}")
        # 考虑不重叠情况，if r1<=start <ennd <= r2 ,即可插入
        if i==0 or self.tasks.items()[i-1][1] <=start:  #寻找前一个区间(l1,r1)，r1<=start
            self.tasks[start] = end
            self.is_merge[start] = False
            # print("没有重叠")
            return True
        # 考虑重叠情况：
        # (l1,r1) 为双重日程，不行。
        # (l1,r1) 不为双重日程，可能行。判断是否与(l0,r0)有交集。
        l1,r1 = self.tasks.items()[i-1]
        if not self.is_merge[l1] and (i-1 <= 0 or (not self.is_merge[self.tasks.items()[i-2][0]] and\
            self.tasks.items()[i-2][1]<=start)):
            s = min(l1,start)
            if l1 != s: self.tasks.pop(l1) #删除合并前的元素
            self.tasks[s] = max(r1,end)
            self.is_merge[s] = True
            # print("二重折叠")
            return True
        return False


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

