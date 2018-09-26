class Solution:
    def __init__(self):
        self.nums = None
        self.n = 0
        self.res = []
        
    def permutation(self, pos):
        nums = self.nums
        if pos == self.n - 1:
            self.res.append(tuple(nums))
            return
        for i in range(pos, self.n):
            nums[pos], nums[i] = nums[i], nums[pos]
            self.permutation(pos + 1)
            nums[i], nums[pos] = nums[pos], nums[i]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(self.nums)
        self.permutation(0)
        return sorted(list(set(self.res)),key=lambda x: x)