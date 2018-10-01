class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        from functools import reduce
        return reduce(lambda x, y: 26*x + y, map(lambda c:ord(c) - ord('A') + 1, s))