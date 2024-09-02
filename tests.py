import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertNotEqual(len(m1._cells), num_rows) 
        self.assertNotEqual(len(m1._cells[0]), num_cols)

    
    def test_large_maze(self):
        num_rows, num_cols = 1000, 1000
        m6 = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(m6._cells), num_rows)
        self.assertEqual(len(m6._cells[0]), num_cols)
    
    def test_entrance_and_exit_walls_removed(self):
        cols = 15
        rows = 13
        m1 = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[cols - 1][rows - 1].has_bottom_wall,
            False,
        )
    
    def test_reset_cells_visited(self):
        rows = 3
        cols = 10
        self.maze = Maze(3, 3, rows, cols, 10, 10)
        self.maze._cells[0][0].visited = True
        self.maze._cells[1][1].visited = True
        self.maze._cells[2][2].visited = True

        self.maze._reset_cells_visited()
        for row in self.maze._cells:
            for cell in row:
                self.assertFalse(cell.visited, "Cell should be reset to not visited")

if __name__ == "__main__":
    unittest.main()