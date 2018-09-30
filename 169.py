class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for num in nums:
            if num not in data:
                data[num] = 1
            else:
                data[num] += 1
        return sorted(data.items(), key=lambda x: -x[1])[0][0]