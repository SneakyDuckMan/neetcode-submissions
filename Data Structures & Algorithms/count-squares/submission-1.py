class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:

        self.counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point

        for p in self.points:

            if abs(x - p[0]) != abs(y - p[1]) or x == p[0] or y == p[1]:
                continue
            
            ans += self.counts[(x, p[1])]*self.counts[(p[0], y)]

        return ans