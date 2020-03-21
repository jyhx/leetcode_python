#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1 or not head:
            return head
        ret = head
        num = k
        while num > 1:
            ret = ret.next 
            if not ret:
                return head
            num -= 1
        cur = head.next
        head.next = self.reverseKGroup(ret.next, k)
        while head != ret:
            temp = cur.next
            cur.next = head
            head = cur
            cur = temp
        return ret
            
# @lc code=end

