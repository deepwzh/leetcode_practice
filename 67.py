class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a,2) + int(b, 2), 'b') # 最简单的写法，否则就要模拟字符串的加法了
        