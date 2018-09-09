"""
思路：由大到小遍历即可，考虑那六种特殊的情况，因情况数较少，直接加入字典处理比较方便
"""
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {
            1: 'I',
            4: 'IV',
            5:'V',
            9: 'IX',
            10:'X',
            40: 'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M',
        }
        res = []
        for n, v in sorted(list(d.items()), key=lambda x: x[0])[::-1]:
            count = int(num) // int(n)
            if count > 0:
                res += [v]* count
                num -= n * count
        return "".join(res)