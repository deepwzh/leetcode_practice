"""
二分查找
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def search(x):
            low = 0
            high = x
            while low <= high:
                mid = (low + high) //2
                if (mid * mid) > x:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        return search(x)
        # return math.floor(math.sqrt(x)) # 肯定不能这么玩，虽然能对