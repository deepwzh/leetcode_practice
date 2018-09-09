"""
思路：与12题相反，仅需要考虑一下那几种特殊情况即可，详情见下边的代码
"""
class Solution:
    def romanToInt(self, s):
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
        d = dict(zip(d.values(), d.keys()))
        print(d)
        res = 0
        cnt = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                c = s[i] + s[i + 1]
                if c in d:
                    res += d[c]
                    i = i + 2
                    continue
            if s[i] in d:
                res += d[s[i]]
                i = i + 1
        return res
        