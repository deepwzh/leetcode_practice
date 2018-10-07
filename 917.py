class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        strs = []
        for c in S:
            if c.isalpha():
                strs.append(c)
        l = len(strs)
        res = []
        pos = 0
        for c in S:
            if not c.isalpha():
                res.append(c)
            else:
                res.append(strs[l - pos - 1])
                pos += 1
        return ''.join(res)