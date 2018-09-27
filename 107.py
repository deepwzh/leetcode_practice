# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from queue import Queue
        if not root:
            return []
        u = []
        level_flag = {}
        u.append(root)
        level_flag[root] = 1
        res = {}
        while u:
            t = u[0]
            u.pop(0)
            flag = level_flag[t]
            if flag in res:
                res[flag].append(t.val)
            else:
                res[flag] = [t.val]
            if t.left:
                level_flag[t.left] = flag + 1
                u.append(t.left)
            if t.right:
                level_flag[t.right] = flag + 1
                u.append(t.right)
        return [u for u in list(res.values())[::-1]]