#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode.cn/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (54.76%)
# Likes:    1229
# Dislikes: 0
# Total Accepted:    543K
# Total Submissions: 990.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [], val = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中的节点数目在范围 [0, 10^4] 内
# 1 
# 0 
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dump1 = ListNode(0,head)
        pre,p = dump1,dump1.next
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = pre.next
            p = p.next
        return dump1.next
# @lc code=end

