from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import Deque, List, Tuple


class Router:

    def __init__(self, memoryLimit: int):
        self.maxLength = memoryLimit
        self.queue: Deque[Tuple[int, int, int]] = deque()

        self.packetCache = defaultdict(int)
        self.entries = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) not in self.packetCache:
            key = (source, destination, timestamp)
            self.queue.append(key)
            self.packetCache[key] += 1
            self.entries[destination].append(timestamp)

            if len(self.queue) > self.maxLength:
                self.deleteFirstPacket()

            return True

        return False

    def deleteFirstPacket(self):
        firstPacket = self.queue.popleft()
        self.packetCache[firstPacket] -= 1

        if not self.packetCache[firstPacket]:
            del self.packetCache[firstPacket]
            self.entries[firstPacket[1]].popleft()

        return firstPacket

    def forwardPacket(self) -> List[int]:
        if len(self.queue):
            return list(self.deleteFirstPacket())

        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect_left(self.entries[destination], startTime)
        right = bisect_right(self.entries[destination], endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
