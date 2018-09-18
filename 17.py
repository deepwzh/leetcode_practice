class Solution:
    def __init__(self):
        self.digits = '' 
        self.dictorary = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.res = []
    def dfs(self, cnt, res):
        if cnt >= len(self.digits):
            self.res.append(''.join(res))
            return
        l = len(self.dictorary[self.digits[cnt]])
        for i in range(l):
            res.append(self.dictorary[self.digits[cnt]][i])
            self.dfs(cnt + 1, res)
            res.pop()
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        if not digits:
            return []
        else:
            self.dfs(0, [])
            return self.res
