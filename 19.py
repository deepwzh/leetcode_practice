# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        target_node = None
        node = head
        length = 0
        while node:
            length = length + 1
            node = node.next
        node = head
        cnt = 0
        if length == n:
            return head.next
        while node:
            cnt = cnt + 1
            if cnt == length - n:
        
                node.next = node.next.next
                break
            node = node.next
        return head