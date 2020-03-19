#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if (l1.val + l2.val < 10):
            ret = ListNode(l1.val + l2.val)
            ret.next = self.addTwoNumbers(l1.next, l2.next)
            return ret
        c = ListNode((l1.val + l2.val) // 10)
        ret = ListNode((l1.val + l2.val) % 10)
        ret.next = self.addTwoNumbers(c, self.addTwoNumbers(l1.next, l2.next))
        return ret

# @lc code=end

