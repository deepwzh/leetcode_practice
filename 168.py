class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        # if n == 1:
        #     return 'A'
        while n >= 1:
            n = n - 1
            res.append(chr((n) % 26 + ord('A')))
            n = n // 26
            print(n)
        return "".join(res[::-1])
        