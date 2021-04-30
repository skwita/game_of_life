import glob
import random
import time


class Grid:
    def __init__(self, num_horizontal: int, num_vertical: int, cur_num_saves: int):
        self.grid = []
        for i in range(int(num_horizontal)):
            self.grid.append([])
            for j in range(int(num_vertical)):
                self.grid[i].append(False)
        self.length = len(self.grid)
        self.length_in = len(self.grid[0])
        self.cur_num_saves = cur_num_saves

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

    def save(self) -> None:
        file = open(f"presets/s{time.time()}.txt", 'w')
        file.write(f"{self.length} {self.length_in} \n")
        for i in range(self.length):
            for j in range(self.length_in):
                file.write(f"{1 if self.grid[i][j] else 0} ")
            file.write(" \n")
        file.close()

    def load(self):
        file = open(glob.glob("presets/s*.txt")[self.cur_num_saves], 'r')
        print(glob.glob("presets/s*.txt")[self.cur_num_saves].split("\\")[1])
        self.cur_num_saves = 0 if self.cur_num_saves == len(glob.glob("presets/s*.txt")) - 1 else self.cur_num_saves + 1
        length, length_in, *_ = file.readline().split(" ")
        new_grid = Grid(length, length_in, self.cur_num_saves)
        for x in range(self.length):
            line = file.readline().split(" ")
            for index, cell in enumerate(line):
                if cell == "1":
                    new_grid.resurrect(x, index)
        file.close()
        return new_grid
