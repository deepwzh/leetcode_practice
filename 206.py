# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _reverseListRecursively(self, node, par_node):
        """
        递归版本
        """
        if not node:
            return par_node   
        new_head_node = self._reverseList(node.next, node)
        node.next = par_node
        return new_head_node
    
    def _reverseListIteratively(self, head):
        """
        循环版本
        """
        node = head
        new_head = ListNode(None)
        while node:
            next_node = node.next
            node.next = new_head.next
            new_head.next = node
            node = next_node
        return new_head.next
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverseListIteratively(head)
        