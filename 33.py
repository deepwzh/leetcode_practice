"""
二分查找变体（Rotated Sorted Array）：
这道题相对于朴素的二分查找，多了一些分类讨论判断
在任意时刻，mid左边和右边必有一边是有序的。
具体代码如下
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if not length:
            return -1
        low = 0
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                if nums[high] >= nums[mid]:
                    high = mid - 1
                else:
                    if nums[low] > target:
                        low = mid + 1
                    else:
                        high = mid - 1
            elif nums[mid] < target:
                if nums[low] <= nums[mid]:
                    low = mid + 1
                else:
                    if nums[high] < target:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                return mid
        return -1