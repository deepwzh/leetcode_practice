# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node = head
        new_head = ListNode(None)
        cur_new_head = new_head
        start_node = new_head
        a = None
        b = None
        i = 1
        while node:
            cur_node = ListNode(node.val)
            
            if i >= m and i <= n:
                if i == m:
                    cur_new_head = cur_node
                cur_node.next = start_node.next
                start_node.next = cur_node
            else:
                cur_new_head.next = cur_node
                cur_new_head = cur_new_head.next
                start_node = cur_new_head
            i = i + 1
            node = node.next
        return new_head.next