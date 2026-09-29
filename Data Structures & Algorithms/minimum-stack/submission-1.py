class MinStack:

    def __init__(self):
        self.st = []
        self.m = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.m or self.m[-1] >= val:
            self.m.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if val == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.m[-1]
