class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s.strip().split(" "))
        return len(s.strip().split(" ")[-1]) 