# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.last_val = None
    
    def preOrder(self, root):
        self.preOrder(root.left)
        
        self.preOrder(root.right)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # self.isValidBST(root.left)
        # print(root.val)
        # self.isValidBST(root.right)
        if not self.isValidBST(root.left):
            return False
        # print(root.val, self.last_val)
        
        if self.last_val is not None and self.last_val >= root.val:
            return False
        self.last_val = root.val
        if not self.isValidBST(root.right):
            return False
        return True