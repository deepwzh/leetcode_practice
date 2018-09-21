"""
简单回溯法,全排列问题
"""
class Solution:
    def __init__(self):
        self.nums = []
        self.size = 0
        self.res = []
        self.tmp = []
    def dfs(self, cnt):
        if cnt >= self.size:
            self.res.append([*self.tmp])
        for i in range(self.size):
            if self.nums[i] in self.tmp:
                continue
            self.tmp.append(self.nums[i])
            self.dfs(cnt + 1)
            self.tmp.pop()
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.size = len(nums)
        self.dfs(0)
        return self.res
        