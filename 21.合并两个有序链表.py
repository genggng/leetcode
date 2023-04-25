#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.34%)
# Likes:    3074
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
# 
# 
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dump1 = ListNode(0)
        p = dump1
        r1,r2 = list1,list2
        while r1 and r2:
            if r1.val <= r2.val:
                p.next = r1
                r1 = r1.next
            else:
                p.next = r2
                r2 = r2.next
            p = p.next
        if r1:
            p.next = r1
        if r2:
            p.next = r2
        return dump1.next
# @lc code=end

