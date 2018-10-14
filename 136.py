class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = sorted(nums)
        for i in range(0, len(nums), 2):
            if i + 1 >= len(num) or num[i] != num[i + 1]:
                return num[i]
        