class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        is_f = False
        if num < 0:
            is_f = True
            num = -num
        cnt = 0
        while num > 1:
            if num%4 != 0:
                return False;
            cnt += 1
            num //= 4
            print(num)
        print(cnt)
        if not is_f:
            return True
        else:
            return False