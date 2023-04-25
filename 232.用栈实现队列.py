#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
# https://leetcode.cn/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (68.53%)
# Likes:    895
# Dislikes: 0
# Total Accepted:    346.2K
# Total Submissions: 505.3K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 
# 实现 MyQueue 类：
# 
# 
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 
# 
# 说明：
# 
# 
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
# 
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 9
# 最多调用 100 次 push、pop、peek 和 empty
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
# 
# 
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.num = 0 

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.num += 1

    def update(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        if not self.out_stack:
            self.update()
        self.num -= 1
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            self.update()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return bool(self.num == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

