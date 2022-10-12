#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        exist_node = False
        while head:
            if head.val in nums_set:
                exist_node = True
            else:
                if exist_node:
                    res += 1
                    exist_node = False
            head = head.next
        if exist_node:
            res += 1
        return res
# @lc code=end

