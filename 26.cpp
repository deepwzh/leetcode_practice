class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        res = []
        for num in nums:
            if num not in s:
                s.add(num)
                res.append(num)
        print(res)
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)