# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g_set = []
        for i in range(10000+1):
            g_set.append(False)
        for i in G:
            g_set[i] = True
        node = head
        cnt = 0
        is_consecutive = False
        while node:
            if not g_set[node.val]:
                is_consecutive = False
            if not is_consecutive and g_set[node.val]:
                is_consecutive = True
                cnt += 1            
            node = node.next
        return cnt