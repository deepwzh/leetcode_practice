# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        new_head = ListNode(None)
        new_node = new_head
        left_p = head
        node = head
        sta = []
        while node:
            sta.append(node)
            node = node.next
        sta = sta[(len(sta) + 1)// 2 : ]
        node = head
        cnt = 0
        while node:
            tmp_node = ListNode(node.val)
            node = node.next
            new_node.next = tmp_node
            new_node = new_node.next
            if len(sta) == 0:
                break
            tmp_node = ListNode(sta[-1].val)
            new_node.next = tmp_node
            new_node = new_node.next
            sta.pop()
        node = head
        new_node = new_head.next
        while node:
            node.val = new_node.val
            node = node.next
            new_node = new_node.next