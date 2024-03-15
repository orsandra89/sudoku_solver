class SudokuSolverNaiveApproach:

    def solveSudokuUsingNaiveApproach(self, grid, row, col):
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if row == self.N - 1 and col == self.N:
            return True

        # Check if column value becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == self.N:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
        if grid[row][col] > 0:
            return self.solveSudokuUsingNaiveApproach(grid, row, col + 1)
        for num in range(1, self.N + 1, 1):

            # Check if it is safe to place
            # the num (1-9) in the
            # given row ,col ->we
            # move to next column
            if self.isSafe(grid, row, col, num):

                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                grid[row][col] = num

                # Checking for next possibility with next
                # column
                if self.solveSudokuUsingNaiveApproach(grid, row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            grid[row][col] = 0
        return False


class SudokuSolverBacktracking:
    # A Backtracking program
    # in Python to solve Sudoku problem

    # A Utility Function to print the Grid
    def print_grid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" "),
            print()

    # Function to Find the entry in
    # the Grid that is still not used
    # Searches the grid to find an
    # entry that is still unassigned. If
    # found, the reference parameters
    # row, col will be set the location
    # that is unassigned, and true is
    # returned. If no unassigned entries
    # remains, false is returned.
    # 'l' is a list variable that has
    # been passed from the solve_sudoku function
    # to keep track of incrementation
    # of Rows and Columns
    def find_empty_location(self, arr, ll):
        for row in range(9):
            for col in range(9):
                if arr[row][col] == 0:
                    ll[0] = row
                    ll[1] = col
                    return True
        return False

    # Returns a boolean which indicates
    # whether any assigned entry
    # in the specified row matches
    # the given number.
    def used_in_row(self, arr, row, num):
        for i in range(9):
            if arr[row][i] == num:
                return True
        return False

    # Returns a boolean which indicates
    # whether any assigned entry
    # in the specified column matches
    # the given number.
    def used_in_col(self, arr, col, num):
        for i in range(9):
            if arr[i][col] == num:
                return True
        return False

    # Returns a boolean which indicates
    # whether any assigned entry
    # within the specified 3x3 box
    # matches the given number
    def used_in_box(self, arr, row, col, num):
        for i in range(3):
            for j in range(3):
                if arr[i + row][j + col] == num:
                    return True
        return False

    # Checks whether it will be legal
    # to assign num to the given row, col
    # Returns a boolean which indicates
    # whether it will be legal to assign
    # num to the given row, col location.
    def check_location_is_safe(self, arr, row, col, num):

        # Check if 'num' is not already
        # placed in current row,
        # current column and current 3x3 box
        return not self.used_in_row(arr, row, num) and (
            not self.used_in_col(arr, col, num)
            and (not self.used_in_box(arr, row - row % 3, col - col % 3, num))
        )

    # Takes a partially filled-in grid
    # and attempts to assign values to
    # all unassigned locations in such a
    # way to meet the requirements
    # for Sudoku solution (non-duplication
    # across rows, columns, and boxes)
    def solve_sudoku(self, arr):

        # 'l' is a list variable that keeps the
        # record of row and col in
        # find_empty_location Function
        l = [0, 0]

        # If there is no unassigned
        # location, we are done
        if not self.find_empty_location(arr, l):
            return True

        # Assigning list values to row and col
        # that we got from the above Function
        row = l[0]
        col = l[1]

        # consider digits 1 to 9
        for num in range(1, 10):

            # if looks promising
            if self.check_location_is_safe(arr, row, col, num):

                # make tentative assignment
                arr[row][col] = num

                # return, if success,
                # ya !
                if self.solve_sudoku(arr):
                    return True

                # failure, unmake & try again
                arr[row][col] = 0

        # this triggers backtracking
        return False

    # The above code has been contributed by Harshit Sidhwa.


grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

sudokuBacktracking = SudokuSolverBacktracking().solve_sudoku(grid)
sudokuNaiveApproach = SudokuSolverNaiveApproach().solveSudokuUsingNaiveApproach(
    grid, 0, 0
)
if sudokuNaiveApproach:
    print(grid)
else:
    print("no solution exists ")

if sudokuBacktracking:
    print(grid)
else:
    print("no solution exists ")
