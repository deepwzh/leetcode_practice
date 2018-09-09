class StockSpanner:

    def __init__(self):
        self.data = []
        self.res = {}

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        cnt = 0
        count = len(self.data)
        self.data.append(price)
        i = len(self.data) - 1
        while i >= 0:
            if self.data[i] <= price:
                if i in self.res:
                    cnt = cnt + self.res[i]
                    # print(i, self.res[i], cnt)
                    i = i - self.res[i]
                else:
                    cnt = cnt + 1
                    i = i - 1
                    # print(cnt)

            else:
                break
        self.res[count] = cnt
        # print(self.res)
        return cnt
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)