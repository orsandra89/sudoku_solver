from grid.grid import Grid
from strategy.sudoku_strategy import SudokuStrategy


class SudokuNaiveApproachStrategy(SudokuStrategy):
    def solveSudoku(self, grid: Grid):
        return self.solveSudokuUsingNaiveApproach(grid, 0, 0)

    def solveSudokuUsingNaiveApproach(self, grid: Grid, row, col):
        # Check if we have reached the 8th row and 9th column (0 indexed matrix) , we are
        # returning true to avoid further backtracking
        N = len(grid.grid)
        if row == N - 1 and col == N:
            return True

        # Check if column value becomes 9 , we move to next row and column start from 0
        if col == N:
            row += 1
            col = 0

        # Check if the current position of the grid already contains value >0, we iterate for next column
        if grid.nonEmptyCell(row, col):
            return self.solveSudokuUsingNaiveApproach(grid, row, col + 1)
        for num in range(1, N + 1, 1):

            # Check if it is safe to place the num (1-9) in the given row ,col ->we
            # move to next column
            if grid.isSafe(row, col, num):

                grid.putNumber(row, col, num)
                # Checking for next possibility with next column
                if self.solveSudokuUsingNaiveApproach(grid, row, col + 1):
                    return True

            grid.putNumber(row, col, 0)
        return False
