#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 结束条件：学生队列中没有喜欢栈顶三明治
        like_count = Counter(students)
        leaf_student = set()  #走的学生
        n = len(students)
        i = 0
        for sandwich in sandwiches:
            if like_count[sandwich] <= 0: #没有学生喜欢栈顶三明治
                break
            while i < n:
                if i not in leaf_student and students[i] == sandwich:
                    like_count[sandwich] -= 1
                    leaf_student.add(i)   
                    i = (i + 1)%n
                    break
                i = (i + 1)%n
        return n - len(leaf_student)
# @lc code=end
print(Solution().countStudents([1,1,0,0],[0,1,0,1]))
