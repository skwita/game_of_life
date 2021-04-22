import random


class Grid:
    def __init__(self, num_horizontal, num_vertical):
        self.grid = []
        for i in range(int(num_horizontal)):
            self.grid.append([])
            for j in range(int(num_vertical)):
                self.grid[i].append(0)

    def change_cell(self, x: int, y: int):
        if self.grid[x][y] == 0:
            self.resurrect(x, y)
        else:
            self.kill(x, y)

    def resurrect(self, x: int, y: int):
        self.grid[x][y] = 1

    def kill(self, x: int, y: int):
        self.grid[x][y] = 0

    def print(self):
        for i in range(len(self.grid)):
            print(str(self.grid[i]))
        print('\n')

    def is_alive(self, x, y):
        return self.grid[x][y] == 1

    def get_neighbours(self, x, y):
        num = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if len(self.grid) > x + i >= 0 and len(self.grid[0]) > y + j >= 0:
                    if self.grid[x + i][y + j] is not None and self.is_alive(x + i, y + j):
                        if i == 0 and j == 0:
                            pass
                        else:
                            num += 1
        return num

    def clear(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.kill(i, j)

    def randomize(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                if random.randint(0, 9) < 2:
                    self.resurrect(i - 1, j - 1)




