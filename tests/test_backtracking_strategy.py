import unittest
import sys

try:
    # print(sys.path)
    sys.path.insert(1, "")
    # print('in first import block')
    from src.grid.grid import Grid
    from src.strategy.backtracking_strategy import SudokuBacktrackingStrategy

    # print('Direct execution of the test')
except ImportError:
    # print(sys.path)
    sys.path.insert(1, "../")
    # print('in second import block')
    from src.grid.grid import Grid
    from src.strategy.backtracking_strategy import SudokuBacktrackingStrategy

    # print('Execution of the script from tests/ dir')
finally:
    print("\nImporting modules from src -> OK ✅\n")


class MyTestCase(unittest.TestCase):

    def addDuration(self, test, elapsed):  # For Python >= 3.12
        pass

    def setUp(self):
        self.gridSolvable = Grid()
        self.strategy = SudokuBacktrackingStrategy()
        self.solvedGrid = [
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9],
        ]

    def test_solving_grid(self):
        result = self.strategy.solveSudoku(self.gridSolvable)
        self.assertEqual(result, True)
        self.assertEqual(self.gridSolvable.grid, self.solvedGrid)


if __name__ == "__main__":
    unittest.main()
