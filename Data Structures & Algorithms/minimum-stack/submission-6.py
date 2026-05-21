class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_num = val
        else:
            self.stack.append(val - self.min_num)
            if val < self.min_num:
                self.min_num = val

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.min_num = self.min_num - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min_num
        else:
            return self.min_num

    def getMin(self) -> int:
        return self.min_num
