import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells_list),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells_list[0]),
            num_rows,
        )
    
    def test_maze_create_cells_2(self):
        num_cols = 2
        num_rows = 1
        m1 = Maze(10, 10, num_rows, num_cols, 100, 100)
        self.assertEqual(
            len(m1.cells_list),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells_list[0]),
            num_rows,
        )

    def test_maze_break_walls(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1.cells_list[0][0].has_top_wall, False)
        self.assertEqual(m1.cells_list[m1.num_cols - 1][m1.num_rows - 1].has_bottom_wall, False)

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10)
        for col in m1.cells_list:
            for cell in col:
                self.assertEqual(cell.visited, False)

        

if __name__ == "__main__":
    unittest.main()

    