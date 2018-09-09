"""
思路：总体思路是通过正则匹配把源字符串分为三部分
比如字符串"  abc1.23eee"
第一部分是"  abc", 第二部分是"1",第三部分是".23eee"
对于第一部分，如果忽略前导空格后仍然包含乱起八糟的字符，则根据题意我们应该返回0
对于第二部分，需要注意的是为空时或者越界时返回0，另外，我们需要结合第一部分判断正负
对于第三部分，直接忽略即可
详细代码如下
"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        a,b,c = re.match("([^0-9]+)?([0-9]+)?([^0-9]+)?", str.lstrip(' ')).groups()
        if not b:
            return 0
        if not a:
           b = int(b) 
        elif a == '-':
            b = -int(b)
        elif a == '+':
            b = int(b)
        else:
            return 0
        if b < -2147483648:
            return -2147483648
        elif b > 2147483647:
            return 2147483647
        return b