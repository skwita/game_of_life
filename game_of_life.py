import random

import pygame
from pygame.locals import *
from grid import Grid


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.speed = speed

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = int(self.width / self.cell_size)
        self.cell_height = int(self.height / self.cell_size)

    def draw_grid(self, cur_grid) -> None:
        for x in range(int(self.width / self.cell_size)):
            for y in range(int(self.height / self.cell_size)):
                if cur_grid.is_alive(x, y):
                    pygame.draw.rect(self.screen, 'gray', (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, (48, 48, 48), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, 'black', (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        cur_grid = game.create_grid()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color((48, 48, 48)))

        running = True
        temp_run = False
        is_pressed = False
        is_alive = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = int(x / self.cell_size)
                    y = int(y / self.cell_size)
                    cur_grid.change_cell(x, y)
                    is_alive = cur_grid.is_alive(x, y)
                    is_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    is_pressed = False

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[K_UP]:
                        cur_grid = self.step(cur_grid)
                    if keys[K_SPACE]:
                        temp_run = not temp_run
                    if keys[K_DELETE]:
                        cur_grid.clear()
                    if keys[K_r]:
                        cur_grid.randomize()

            if is_pressed:
                x, y = pygame.mouse.get_pos()
                x = int(x / self.cell_size)
                y = int(y / self.cell_size)
                if not is_alive:
                    cur_grid.kill(x, y)
                else:
                    cur_grid.resurrect(x, y)

            if temp_run:
                cur_grid = self.step(cur_grid)

            self.draw_grid(cur_grid)
            pygame.display.flip()
        pygame.quit()

    def create_grid(self) -> Grid:
        return Grid(self.width / self.cell_size, self.height / self.cell_size)

    def step(self, cur_grid):
        new_grid = self.create_grid()
        for i in range(int(self.width / self.cell_size)):
            for j in range(int(self.height / self.cell_size)):
                num = cur_grid.get_neighbours(i, j)
                alive = cur_grid.is_alive(i, j)
                if alive:
                    if 1 < num < 4:
                        new_grid.resurrect(i, j)
                    else:
                        new_grid.kill(i, j)
                else:
                    if num == 3:
                        new_grid.resurrect(i, j)
                    else:
                        new_grid.kill(i, j)
        return new_grid


if __name__ == '__main__':
    # game = GameOfLife(1920, 1000, 10)
    game = GameOfLife(1000, 1000, 10)
    game.run()
