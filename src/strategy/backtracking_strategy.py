from grid.grid import Grid
from strategy.sudoku_strategy import SudokuStrategy


class SudokuBacktrackingStrategy(SudokuStrategy):

    def solveSudoku(self, grid: Grid):

        # 'l' is a list variable that keeps the record of row and col in
        l = grid.l

        if (not grid.find_empty_location(l)):
            return True

        row = l[0]
        col = l[1]

        for num in range(1, 10):

            if (grid.isSafe( row, col, num)):

                grid.grid[row][col] = num

                if (self.solveSudoku(grid)):
                    return True

                grid.grid[row][col] = 0

        return False