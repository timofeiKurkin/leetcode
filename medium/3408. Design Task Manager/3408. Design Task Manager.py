import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.hp = []
        self.taskPriority = {}
        self.taskOwner = {}

        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.hp, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.hp, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.taskPriority[taskId] = -1

    def execTop(self) -> int:
        while self.hp:
            priority, taskId = heapq.heappop(self.hp)
            if self.taskPriority.get(-taskId, -2) == -priority:
                self.taskPriority[-taskId] = -1
                return self.taskOwner.get(-taskId, -1)

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
