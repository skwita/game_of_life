import random

import pygame
from pygame.locals import *
from grid import Grid


def main(cur_game):
    cur_game.run(cur_game)


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.speed = speed

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.num_cell_horizontal = int(self.width / self.cell_size)
        self.num_cell_vertical = int(self.height / self.cell_size)

    def run(self, cur_game):
        pygame.init()
        cur_grid = cur_game.create_grid()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color((48, 48, 48)))

        is_game_running = True
        is_running = False
        is_mouse_btn_pressed = False
        is_clicked_alive = False

        while is_game_running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    is_game_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x = int(x / self.cell_size)
                    y = int(y / self.cell_size)
                    cur_grid.change_cell(x, y)
                    is_clicked_alive = cur_grid.is_alive(x, y)
                    is_mouse_btn_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    is_mouse_btn_pressed = False

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[K_UP]:
                        cur_grid = self.step(cur_grid)
                    if keys[K_SPACE]:
                        is_running = not is_running
                    if keys[K_DELETE]:
                        cur_grid.clear()
                    if keys[K_r]:
                        cur_grid.randomize()

            if is_mouse_btn_pressed:
                x, y = pygame.mouse.get_pos()
                x = int(x / self.cell_size)
                y = int(y / self.cell_size)
                if not is_clicked_alive:
                    cur_grid.kill(x, y)
                else:
                    cur_grid.resurrect(x, y)

            if is_running:
                cur_grid = self.step(cur_grid)

            self.draw_grid(cur_grid)
            pygame.display.flip()
        pygame.quit()

    def draw_grid(self, cur_grid):
        for x in range(self.num_cell_horizontal):
            for y in range(self.num_cell_vertical):
                if cur_grid.is_alive(x, y):
                    i = random.randint(-20, 20)
                    j = random.randint(-20, 20)
                    k = random.randint(-20, 20)
                    a, b, c = 149, 52, 235  # (purple)
                    pygame.draw.rect(self.screen, (a + i, b + j, c + k),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, (48, 48, 48),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, 'black', (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, 'black', (0, y), (self.width, y))

    def step(self, cur_grid):
        new_grid = self.create_grid()
        for i in range(self.num_cell_horizontal):
            for j in range(self.num_cell_vertical):
                num = cur_grid.get_neighbours(i, j)
                alive = cur_grid.is_alive(i, j)
                if alive:
                    if 1 < num < 4:
                        new_grid.resurrect(i, j)
                        continue
                    new_grid.kill(i, j)
                if num == 3:
                    new_grid.resurrect(i, j)
                    continue
                new_grid.kill(i, j)
        return new_grid

    def create_grid(self):
        return Grid(self.num_cell_horizontal, self.num_cell_vertical)


if __name__ == '__main__':
    game = GameOfLife(1000, 1000, 10)
    main(game)
