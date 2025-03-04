import random


class RandomizedSet:

    def __init__(self):
        self.lst: list[int] = []
        self.obj: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.obj:
            return False

        self.lst.append(val)
        self.obj[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.obj:
            idx_to_remove = self.obj[val]
            lastElement = self.lst[-1]

            self.lst[idx_to_remove] = lastElement
            self.obj[lastElement] = idx_to_remove

            self.lst.pop()
            del self.obj[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(list(self.obj))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
