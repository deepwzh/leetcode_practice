class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = [1]
        for i in range(n-1):
            res.append('-')
            new_res = []
            last_c = res[0]
            cnt = 0
            for j in range(len(res)):
                if res[j] != last_c:
                    new_res.append(cnt)
                    new_res.append(last_c)
                    cnt = 1
                else:
                    cnt = cnt + 1
                last_c = res[j]
            res = new_res
        return ''.join([str(v) for v in res])
            