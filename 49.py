from collections import defaultdict
class Solution:
    def hash(self, v):
        r = sorted(v)
        res = 0
        for i in range(len(r)):
            res += (ord(r[i]) - ord('a'))*(26**i)
        return res
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_dict = defaultdict(list)
        for str in strs:
            hash_dict[self.hash(str)].append(str)
        return [sorted(hash_dict[key], key=lambda x: x) for key in hash_dict]