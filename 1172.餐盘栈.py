#
# @lc app=leetcode.cn id=1172 lang=python3
#
# [1172] 餐盘栈
#
# https://leetcode.cn/problems/dinner-plate-stacks/description/
#
# algorithms
# Hard (28.60%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 18.7K
# Testcase Example:  '["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]\n' +
#  '[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]'
#
# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
#
# 实现一个叫「餐盘」的类 DinnerPlates：
#
#
# DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
# void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
# int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
# int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回
# -1。
#
#
#
#
# 示例：
#
# 输入：
#
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# 输出：
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
#
# 解释：
# DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // 栈的现状为：    2  4
# 1  3  5
# ⁠                                   ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 2。栈的现状为：      4
# ⁠                                         1  3  5
# ⁠                                         ﹈ ﹈ ﹈
# D.push(20);        // 栈的现状为：  20  4
# 1  3  5
# ⁠                                  ﹈ ﹈ ﹈
# D.push(21);        // 栈的现状为：  20  4 21
# 1  3  5
# ⁠                                  ﹈ ﹈ ﹈
# D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
# ⁠                                           1  3  5
# ⁠                                           ﹈ ﹈ ﹈
# D.popAtStack(2);   // 返回 21。栈的现状为：       4
# ⁠                                           1  3  5
# ⁠                                           ﹈ ﹈ ﹈
# D.pop()            // 返回 5。栈的现状为：        4
# ⁠                                           1  3
# ⁠                                           ﹈ ﹈
# D.pop()            // 返回 4。栈的现状为：    1  3
# ⁠                                          ﹈ ﹈
# D.pop()            // 返回 3。栈的现状为：    1
# ⁠                                          ﹈
# D.pop()            // 返回 1。现在没有栈。
# D.pop()            // 返回 -1。仍然没有栈。
#
#
#
#
# 提示：
#
#
# 1 <= capacity <= 20000
# 1 <= val <= 20000
# 0 <= index <= 100000
# 最多会对 push，pop，和 popAtStack 进行 200000 次调用。
#
#
#
import heapq
# @lc code=start


# class DinnerPlates:

#     def __init__(self, capacity: int):
#         self.main_q = []
#         self.capacity = capacity
#         self.empty_stack = heapq.heapify([])
#     def push(self, val: int) -> None:
#         if not self.main_q:
#             self.main_q.append([])
#             heapq.heappush(self.empty_stack,0)
#         min_idx = heapq.heappop()
#         stack = self.main_q[min_idx]
#         if len(head) < self.capacity:
#             head.append(val)
#         else:
#             self.main_q.append([val])

#     def pop(self) -> int:
#         while self.main_q:
#             tail = self.main_q[-1]
#             if not tail:
#                 self.main_q.pop()
#             else:
#                 break
#         if not self.main_q:
#             return -1
        
#         val = tail.pop()
#         if not tail:
#             self.main_q.pop()
#         return val

#     def popAtStack(self, index: int) -> int:
#         if not self.main_q or index >= len(self.main_q) or not self.main_q[index]:
#             return -1
#         val = self.main_q[index].pop()
#         return val

from sortedcontainers import *
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.top = []
        self.poppedPos = SortedSet()

    def push(self, val: int) -> None:
        if not self.poppedPos:
            pos = len(self.stack)
            self.stack.append(val)
            if pos % self.capacity == 0:
                self.top.append(0)
            else:
                stackPos = len(self.top) - 1
                stackTop = self.top[stackPos]
                self.top[stackPos] = stackTop + 1
        else:
            pos = self.poppedPos.pop(0)
            self.stack[pos] = val
            index = pos // self.capacity
            stackTop = self.top[index]
            self.top[index] = stackTop + 1

    def pop(self) -> int:
        while self.stack and self.poppedPos and self.poppedPos[-1] == len(self.stack) - 1:
            self.stack.pop()
            pos = self.poppedPos.pop()
            if pos % self.capacity == 0:
                self.top.pop()
        if not self.stack:
            return -1
        else:
            pos = len(self.stack) - 1
            val = self.stack[pos]
            self.stack.pop()
            if pos % self.capacity == 0 and self.top:
                self.top.pop()
            elif self.top:
                self.top[-1] -= 1
            return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.top):
            return -1
        stackTop = self.top[index]
        if stackTop < 0:
            return -1
        self.top[index] = stackTop - 1
        pos = index * self.capacity + stackTop
        self.poppedPos.add(pos)
        return self.stack[pos]
# Your DinnerPlates object will be instantiated and called as such:

# @lc code=end
D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)       
D.popAtStack(0)
D.push(20)
D.push(21)
D.popAtStack(0)
D.popAtStack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()

