import pygame
import numpy as np
import ctypes
from PIL import Image, ImageDraw, ImageShow
class GameofLife:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=0, active_color=(140, 140, 140), inactive_color=(28, 84, 67), ii=0):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.columns = int(height / scale)
        self.rows = int(width / scale)
        self.ii = ii
        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def run(self):
        """"Update and redraw the current grid state"""
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        """Drawing the grid"""
        out = Image.new("RGB", (self.width, self.height), self.inactive_color)
        draw = ImageDraw.Draw(out);
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    draw.rectangle([row * self.scale, col * self.scale,row * self.scale + self.scale, col * self.scale + self.scale], self.active_color)
                    pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    draw.rectangle([row * self.scale, col * self.scale,row * self.scale + self.scale, col * self.scale + self.scale], self.inactive_color)
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
        out.save(str(self.ii)+"temp.png", format="png")
        self.ii += 1
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "temp.bmp", 0)

    def update_grid(self):
        """Updating the grid based on Conway's game of life rules"""
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid


    def update_cell(self, x, y):
        """Update single cell based on Conway's game of life rules"""
        current_state = self.grid[x, y]
        alive_neighbors = 0

        # Get to how many alive neighbors
        for i in range(-1, 2):
            if ((x + i) < 0 or ((x + i) >= self.grid.shape[0])):
                continue
            for j in range(-1, 2):
                if ((y + j) < 0 or (y + j) >= self.grid.shape[1]):
                    continue
                if i == 0 and j == 0:
                        continue
                elif self.grid[x + i, y + j]:
                    alive_neighbors += 1
        # Updating the cell's state
        if current_state and alive_neighbors < 2:                                       # dies as if by underpopulation
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):          # lives to the next generation
            return True
        elif current_state and alive_neighbors > 3:                                     # dies as if by overpopulation
            return False
        elif ~current_state and alive_neighbors == 3:                                   # becomes alive as if by reproduction
            return True
        else:
            return current_state