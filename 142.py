"""
快慢指针，证明详见百度
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        high = head
        low = head
        p = None
        while low and high: 
            low = low.next
            high = high.next
            if not high:
                return None
            high = high.next
            if high == low:
                p = low
                break
        if not p:
            return None
        res = head
        while p != None:
            if res == p:
                return res
            res = res.next
            p = p.next
        return None