"""
快速幂
"""
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        is_fu = False
        if n < 0:
            is_fu = True
            n = - n
        r = 1
        base = x
        while n != 0:
            if n % 2 == 1:
                r = r * base
            base = base * base
            n = n // 2
        if is_fu:
            return 1 / r
        else:
            return r
        # return x**n 肯定不能这么玩，虽然这么玩能对