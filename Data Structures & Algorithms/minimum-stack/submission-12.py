class MinStack:

    def __init__(self):
        self.stack = []
        self.min_prev = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_prev:
            self.min_prev.append(val)
        else:
            self.min_prev.append(min(val, self.min_prev[-1]))

    def pop(self) -> None:
        pop = self.stack.pop()
        self.min_prev.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_prev[-1]
