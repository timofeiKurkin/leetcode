from collections import deque


class MinStack:
    stack: deque[int]
    minStack: deque[int]

    def __init__(self):
        self.stack = deque([])
        self.minStack = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not len(self.minStack):
            self.minStack(val)
            return
        self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
