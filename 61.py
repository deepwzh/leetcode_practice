# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        u = list()
        node = head
        cnt = 0
        while node:
            u.append(node)
            node = node.next
            cnt = cnt + 1
        if not cnt:
            return head
        k = k % cnt
        for i in range(cnt - 1, cnt - 1 - k, -1):
            u[i - 1].next = None
            u[i].next = head
            head = u[i]
        return head