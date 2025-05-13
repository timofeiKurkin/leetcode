class RecentCounter:

    def __init__(self):
        self.requests = []
        self.prev_start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        time_range = t - 3000

        start = self.prev_start
        while self.requests[start] < time_range:
            start += 1

        self.prev_start = start
        return len(self.requests) - start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
