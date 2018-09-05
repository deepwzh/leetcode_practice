class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        res = repr(x)
        if res[0] == '-':
            res =res[1:] + "-"
        num = int(re.sub("(?<!\d)0+(?!$)", "", res[::-1]))
        if num < -2**31 or num > 2**31 - 1:
            return 0
        else:
            return num