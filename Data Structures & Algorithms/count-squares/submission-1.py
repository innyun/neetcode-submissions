class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        squares = 0
        for k, v in self.points.items():
            double = v
            if abs(k[0] - point[0]) == abs(k[1] - point[1]) and k[0] != point[0]:
                if (k[0], point[1]) in self.points and (point[0], k[1]) in self.points:
                    squares += self.points[(k[0], point[1])] * self.points[(point[0], k[1])] * v

        return squares
