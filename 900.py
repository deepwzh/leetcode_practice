class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.data = []
        self.num = []
        self.value = []
        self.cnt = -1
        self.amount = 0
        for i in range(0, len(A), 2):
            self.num.append(A[i])
            self.value.append(A[i+1])
            self.amount = self.amount + A[i]
            # self.data = self.data + [A[i+1]] * A[i] 

        
    def get_value(self, cnt):
        cur_cnt = cnt
        for i in range(len(self.num)):
            if cur_cnt >= self.num[i]: 
                cur_cnt = cur_cnt - self.num[i]
            else:
                return self.value[i]
    
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = self.cnt + n
        if self.cnt >= self.amount:
            return -1
        else:
            return self.get_value(self.cnt)
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)