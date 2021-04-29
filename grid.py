import random


class Grid:
    def __init__(self, num_horizontal: int, num_vertical: int):
        self.grid = []
        for i in range(int(num_horizontal)):
            self.grid.append([])
            for j in range(int(num_vertical)):
                self.grid[i].append(False)
        self.length = len(self.grid)
        self.length_in = len(self.grid[0])

    def change_cell(self, x: int, y: int) -> None:
        self.grid[x][y] = not self.grid[x][y]

    def resurrect(self, x: int, y: int) -> None:
        self.grid[x][y] = True

    def kill(self, x: int, y: int) -> None:
        self.grid[x][y] = False

    def is_alive(self, x: int, y: int) -> bool:
        return self.grid[x][y]

    def get_neighbours(self, x: int, y: int) -> int:
        num = 0
        num += 1 if self.length > x - 1 >= 0 and self.length_in > y - 1 >= 0 and self.grid[x - 1][y - 1] else 0
        num += 1 if self.length > x - 1 >= 0 and self.length_in > y + 0 >= 0 and self.grid[x - 1][y + 0] else 0
        num += 1 if self.length > x - 1 >= 0 and self.length_in > y + 1 >= 0 and self.grid[x - 1][y + 1] else 0
        num += 1 if self.length > x + 0 >= 0 and self.length_in > y - 1 >= 0 and self.grid[x + 0][y - 1] else 0
        num += 1 if self.length > x + 0 >= 0 and self.length_in > y + 1 >= 0 and self.grid[x + 0][y + 1] else 0
        num += 1 if self.length > x + 1 >= 0 and self.length_in > y - 1 >= 0 and self.grid[x + 1][y - 1] else 0
        num += 1 if self.length > x + 1 >= 0 and self.length_in > y + 0 >= 0 and self.grid[x + 1][y + 0] else 0
        num += 1 if self.length > x + 1 >= 0 and self.length_in > y + 1 >= 0 and self.grid[x + 1][y + 1] else 0
        return num

    def clear(self) -> None:
        for i in range(self.length):
            for j in range(self.length_in):
                self.kill(i, j)

    def randomize(self) -> None:
        for i in range(0, self.length):
            for j in range(0, self.length_in):
                if random.randint(0, 9) < 2:
                    self.resurrect(i, j)
