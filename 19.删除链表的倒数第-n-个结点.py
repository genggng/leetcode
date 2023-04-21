#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = p =  ListNode(0,head)
        r = head
        for _ in range(n):
            r = r.next
        while r:
            r = r.next
            p = p.next
        p.next = p.next.next
        return d.next

# @lc code=end

