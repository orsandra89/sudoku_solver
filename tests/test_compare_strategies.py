import unittest
import sys
from copy import copy, deepcopy
import time


try:
    # print(sys.path)
    sys.path.insert(1, "")
    # print('in first import block')
    from src.grid.grid import Grid
    from src.strategy.bitmask_strategy import BitmaskStrategy
    from src.strategy.naive_approach_strategy import SudokuNaiveApproachStrategy
    from src.strategy.backtracking_strategy import SudokuBacktrackingStrategy
    from src.strategy.cross_hatching_and_backtracing_strategy import (
        CrossHatchingAndBacktracingStrategy,
    )

    # print('Direct execution of the test')
except ImportError:
    # print(sys.path)
    sys.path.insert(1, "../")
    # print('in second import block')
    from src.grid.grid import Grid
    from src.strategy.bitmask_strategy import BitmaskStrategy
    from src.strategy.naive_approach_strategy import SudokuNaiveApproachStrategy
    from src.strategy.backtracking_strategy import SudokuBacktrackingStrategy
    from src.strategy.cross_hatching_and_backtracing_strategy import (
        CrossHatchingAndBacktracingStrategy,
    )

    # print('Execution of the script from tests/ dir')
finally:
    print("\nImporting modules from src -> OK ✅\n")


class MyTestCase(unittest.TestCase):

    def addDuration(self, test, elapsed):  # For Python >= 3.12
        pass

    def setUp(self):
        self.gridSolvable = Grid()
        self.bitmaskStrategy = BitmaskStrategy()
        self.naiveStrategy = SudokuNaiveApproachStrategy()
        self.backtrackingStrategy = SudokuBacktrackingStrategy()
        self.crossHatchingAndBacktrackingStrategy = (
            CrossHatchingAndBacktracingStrategy()
        )
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
        print("start comparing algorithms")

        print("NaiveStrategy")
        self.executeFunctionWithTimeCalculation(
            self.naiveStrategy.solveSudoku, self.gridSolvable, 10000
        )
        print("BacktrackingStrategy")
        self.executeFunctionWithTimeCalculation(
            self.backtrackingStrategy.solveSudoku, self.gridSolvable, 10000
        )
        print("BitmaskStrategy")
        self.executeFunctionWithTimeCalculation(
            self.bitmaskStrategy.solveSudoku, self.gridSolvable, 10000
        )
        print("CrossHatchingAndBacktrackingStrategy")
        self.executeFunctionWithTimeCalculation(
            self.crossHatchingAndBacktrackingStrategy.solveSudoku,
            self.gridSolvable,
            10000,
        )

    def executeFunctionWithTimeCalculation(self, fn, data, n):
        start_time = time.time()
        for _ in range(n):
            fn(deepcopy(data))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: ", elapsed_time)


if __name__ == "__main__":
    unittest.main()
