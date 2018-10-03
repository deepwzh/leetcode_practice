class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        new_head = ListNode(None)
        cur_new_head = new_head
        last_val = None
        while node:
            if node.val != last_val and (not node.next or node.val != node.next.val):
                cur_new_head.next = node
                cur_new_head = cur_new_head.next 
            last_val = node.val
            node = node.next
            cur_new_head.next = None
        return new_head.next