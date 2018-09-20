class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = [num for num in nums if num != val]
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)