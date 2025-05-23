import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1, 1000 + 1)]
        self.nums = set(self.h)
        heapq.heapify(self.h)

    def popSmallest(self) -> int:
        v = heapq.heappop(self.h)
        self.nums.remove(v)
        return v

    def addBack(self, num: int) -> None:
        if num in self.nums:
            return

        self.nums.add(num)
        heapq.heappush(self.h, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
