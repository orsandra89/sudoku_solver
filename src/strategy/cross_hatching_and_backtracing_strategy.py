from grid.grid import Grid
from strategy.sudoku_strategy import SudokuStrategy


class CrossHatchingAndBacktracingStrategy(SudokuStrategy):
    pos = {}
    rem = {}
    graph = {}
    def solveSudoku(self, grid: Grid):
        self.build_pos_and_rem(grid)

        # Sort the rem map in order to start with smaller number of elements to be filled first. Optimization for pruning
        self.rem = {k: v for k, v in sorted(self.rem.items(), key=lambda item: item[1])}

        self.build_graph(grid)

        key_s = list(self.rem.keys())
        # Util called to fill the matrix
        return self.fill_matrix(grid,0, key_s, 0, list(self.graph[key_s[0]].keys()))

    def fill_matrix(self, grid: Grid, k, keys, r, rows):
        for c in self.graph[keys[k]][rows[r]]:
            if grid.nonEmptyCell(rows[r], c):
                continue

            if grid.isSafe(rows[r], c, keys[k]):
                grid.grid[rows[r]][c] = keys[k]
                if r < len(rows) - 1:
                    if self.fill_matrix(grid, k, keys, r + 1, rows):
                        return True
                    else:
                        grid.grid[rows[r]][c] = 0
                        continue
                else:
                    if k < len(keys) - 1:
                        if self.fill_matrix(grid, k + 1, keys, 0, list(self.graph[keys[k + 1]].keys())):
                            return True
                        else:
                            grid.grid[rows[r]][c] = 0
                            continue
                    return True
            grid.grid[rows[r]][c] = 0
        return False

    # Fill the pos and rem dictionary. It will be used to build graph
    def build_pos_and_rem(self, grid: Grid):
        for i in range(0, len(grid.grid)):
            for j in range(0, len(grid.grid)):
                if grid.grid[i][j] > 0:
                    if grid.grid[i][j] not in self.pos:
                        self.pos[grid.grid[i][j]] = []
                    self.pos[grid.grid[i][j]].append([i, j])
                    if grid.grid[i][j] not in self.rem:
                        self.rem[grid.grid[i][j]] = 9
                    self.rem[grid.grid[i][j]] -= 1

        # Fill the elements not present in input matrix. Example: 1 is missing in input matrix
        for i in range(1, 10):
            if i not in self.pos:
                self.pos[i] = []
            if i not in self.rem:
                self.rem[i] = 9

    # Build the graph

    def build_graph(self, grid: Grid):
        for k, v in self.pos.items():
            if k not in self.graph:
                self.graph[k] = {}

            row = list(range(0, 9))
            col = list(range(0, 9))

            for cord in v:
                row.remove(cord[0])
                col.remove(cord[1])

            if len(row) == 0 or len(col) == 0:
                continue

            for r in row:
                for c in col:
                    if grid.grid[r][c] == 0:
                        if r not in self.graph[k]:
                            self.graph[k][r] = []
                        self.graph[k][r].append(c)
