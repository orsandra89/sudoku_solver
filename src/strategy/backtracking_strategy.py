from grid.grid import Grid
from strategy.sudoku_strategy import SudokuStrategy


class SudokuBacktrackingStrategy(SudokuStrategy):

    def solveSudoku(self, grid: Grid):

        # 'empty_position' is a list variable that keeps the record of row and col in
        empty_position = grid.find_empty_location()

        if not empty_position:
            return True

        row = empty_position[0]
        col = empty_position[1]

        for num in range(1, 10):

            if grid.isSafe(row, col, num):

                grid.putNumber(row, col, num)

                if self.solveSudoku(grid):
                    return True

                grid.cleanCell(row, col)

        return False
