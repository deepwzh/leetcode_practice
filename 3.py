class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = dict()
        max_v = 0
        start = 0
        for i in range(len(s)):
            # 记录与当前字符相同的前一个位置，此处需要注意，当记录的位置小于开始位置时，需要使之失效
            if s[i] in q and q[s[i]] >= start:
                start = q[s[i]] + 1
            q[s[i]] = i
            max_v = max(max_v, i - start + 1)
        return max_v