class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        A = [c for c in A]
        B = [c for c in B]
        l = len(A)
        ll = len(B)
        if not l and not ll:
            return True
        if not l or not ll:
            return False
        for i in range(l):
            if A[i:] + A[0:i] == B:
                return True
        return False
            