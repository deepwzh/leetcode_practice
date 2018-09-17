"""
大数据不能通过
"""
def low_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start
def high_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end
class Solution:
    def search(self, nums, target, selected):
        low = low_search(nums, target)
        high = high_search(nums, target)
        self.cache_high[target] = high
        for i in range(low, high + 1):
            if i not in selected:
                return i
        return -1
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums = sorted(nums)
        nums_size = len(nums)
        for i in range(nums_size):
            for j in range(i+1, nums_size):
                pos = self.search(nums, -(nums[i] + nums[j]), [i, j])
                if pos != -1:
                    res.add(tuple(sorted([nums[i], nums[j], nums[pos]])))
        return sorted(list(res))