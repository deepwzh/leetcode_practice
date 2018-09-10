# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # print(not l1, not l2)
        head = None
        node1 = l1
        node2 = l2
        node = None
        if not l1 and not l2:
            return []
        if not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        if l1.val < l2.val:
            head = ListNode(node1.val)
            node1 = node1.next
        else:
            head = ListNode(node2.val)
            node2 = node2.next
        node = head
        while node1 and node2:
            if node1.val < node2.val:
                node.next = ListNode(node1.val)
                node1 = node1.next
            else:
                node.next = ListNode(node2.val)
                node2 = node2.next
            node = node.next
        if node1:
            node.next = node1
        else:
            node.next = node2
        return head