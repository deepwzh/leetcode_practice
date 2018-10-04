# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        greater_list = ListNode(None)
        less_list = ListNode(None)
        greater_node = greater_list
        less_node = less_list
        node = head
        while node:
            newnode = ListNode(node.val)
            if node.val < x:
                less_node.next = newnode
                less_node = less_node.next
            else:
                greater_node.next = newnode
                greater_node = greater_node.next
            less_node.next = greater_list.next
            node = node.next
        if less_list.next:
            return less_list.next
        else:
            return greater_list.next