from abc import ABC, abstractmethod

from grid.grid import Grid


class SudokuStrategy(ABC):

    @abstractmethod
    def solveSudoku(self, grid: Grid):
        pass
