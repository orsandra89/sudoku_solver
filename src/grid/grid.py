class Grid:
    def __init__(self):
        self.grid = [
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
        self.l = [0, 0]

    def printGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                print(self.grid[i][j], end=" ")
            print()

    def isSafe(self, row, col, num):

        # Check if we find the same num in the similar row , we return false
        for x in range(len(self.grid)):
            if self.grid[row][x] == num:
                return False

        # Check if we find the same num in the similar column , we return false
        for x in range(len(self.grid)):
            if self.grid[x][col] == num:
                return False

        # Check if we find the same num in the particular 3*3 matrix, we return false
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def putNumber(self, row, col, num):
        self.grid[row][col] = num

    def emptyCell(self, row, col):
        return self.grid[row][col] == 0

    def nonEmptyCell(self, row, col):
        return not self.emptyCell(row, col)

    def find_empty_location(self, l):
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if (self.grid[row][col] == 0):
                    l[0] = row
                    l[1] = col
                    return True
        return False