#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = [head for head in lists if head]
        if not heads:
            return []
        head = min(heads, key=lambda x: x.val)
        heads.pop(heads.index(head))
        if head.next:
            heads.append(head.next)
        cur = head
        while heads:
            cur.next = min(heads, key=lambda x: x.val)
            heads.pop(heads.index(cur.next))
            cur = cur.next
            if cur.next:
                heads.append(cur.next)
        return head

# @lc code=end
