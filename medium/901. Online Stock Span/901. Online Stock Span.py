class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][1] > price:
            self.stack.append([1, price])
            return 1
        else:
            span = 0
            while self.stack and self.stack[-1][1] <= price:
                span += self.stack.pop()[0]

            self.stack.append([span + 1, price])
            return span + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
