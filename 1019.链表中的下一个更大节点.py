#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 这种做法会超时
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # n = len(res)
        # for i in range(n):
        #     num = res[i]
        #     res[i] = 0
        #     for j in range(i+1,n):
        #         if res[j] > num:
        #             res[i] = res[j]
        #             break
        # return res

        # 单调栈，存放单调递减的元素
        st = []
        res = []
        cur = head
        while cur:
            res.append(0)
            cur_idx = len(res) - 1
            while st and cur.val > st[-1][0].val: #比栈顶元素大，出栈
                node,idx = st.pop()
                res[idx] = cur.val
            st.append((cur,cur_idx)) #栈中比cur小的值都出栈，把当前节点进栈
            cur = cur.next
        return res



# @lc code=end
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)

print(Solution().nextLargerNodes(head))
