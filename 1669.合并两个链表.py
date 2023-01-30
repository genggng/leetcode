#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h2,t2 = list2,list2
        while t2.next:
            t2 = t2.next
        t = list1
        for i in range(b+1):
            # print(t.val)
            if i == a-1:
                p = t.next
                t.next = h2
                t = p
                continue
            if i == b:
                t2.next = t.next
                t.next = None
                break                
            t = t.next
        return list1

# @lc code=end


