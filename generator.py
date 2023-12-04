from random import randint, shuffle
from solver import Solver

class Generator:
    def __init__(self):
        self.__solver = Solver()
        self.__DIFFICULTY = {
        "pvp":         62,
        "pve":       53,
        }
        self.__listNum = [1,2,3,4,5,6,7,8,9]
    def fillGrid(self, grid):
        pos = self.__solver.nextpos(grid)
        shuffle(self.__listNum)
        if not pos:
            return True
        for n in self.__listNum:
             if not self.__solver.exists(grid, n, pos):
                grid[pos[0]][pos[1]] = n
                if self.fillGrid(grid):
                    return True
                grid[pos[0]][pos[1]] = 0
        return False

    def generate(self, difficulty):
        grid = [[0 for r in range(9)] for c in range(9)]
        self.fillGrid(grid)
        for i in range(0, 81 - int(self.__DIFFICULTY[difficulty])):
            row = randint(0,8)
            col = randint(0,8)
            while grid[row][col]==0:
                row = randint(0,8)
                col = randint(0,8)
            grid[row][col]=0
        return grid