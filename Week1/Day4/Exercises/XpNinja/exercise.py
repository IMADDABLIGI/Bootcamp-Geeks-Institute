import time
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state):
        self.rows = rows
        self.cols = cols
        self.grid = initial_state

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")  # Clears the terminal screen
        for row in self.grid:
            print(" ".join("⬛" if cell else "⬜" for cell in row))
        print()

    def count_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r][c]
        return count

    def update(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.count_neighbors(row, col)
                if self.grid[row][col] == 1:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = 1
                else:
                    if neighbors == 3:
                        new_grid[row][col] = 1
        self.grid = new_grid

    def run(self, generations=10, delay=1):
        for _ in range(generations):
            self.display()
            self.update()
            time.sleep(delay)

# Define initial state (5x5 grid)
initial_state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

game = GameOfLife(5, 5, initial_state)
game.run(generations=10, delay=0.5)
