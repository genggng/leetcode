#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#
import heapq
# @lc code=start
# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 使用栈来管理当前通过率最低的班级
        # 每次都选取通过率最低的班级
        # score = []
        # for passes,total in classes:
        #     score.append((passes/total,passes,total))
        # heapq.heapify(score)
        # while extraStudents>0:
        #     _,passes,total = heapq.heappop(score)
        #     heapq.heappush(score,((passes+1)/(total+1),passes+1,total+1))
        #     extraStudents -= 1
        # return sum([s[0] for s in score]) / len(score)

        #  每个优秀学生带来的绝对提升=1/班级人数/班级数
        #  把优秀学生给班级人数最少的，通过率未满的班级。
        # score = []
        # for passes,total in classes:
        #     score.append((total,passes))
        # heapq.heapify(score)
        # while extraStudents>0:
        #     total,passes = heapq.heappop(score)
        #     heapq.heappush(score,(total+1,passes+1))
        #     extraStudents -= 1
        # return sum([p/t for t,p in score]) / len(score)

        # 单个优秀生带来的贡献率提升，i<j：(self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)
class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)


# @lc code=end

