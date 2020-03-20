#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        del_pre = head
        while n > 0:
            p = p.next
            n -= 1
        # 删除头结点
        if not p:
            return head.next
        else:
            p = p.next

        while p:
            p = p.next
            del_pre = del_pre.next
        del_pre.next = del_pre.next.next if del_pre.next else None
        return head

# @lc code=end
