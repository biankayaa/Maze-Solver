import time
from cells import Cell
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None): 
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        if seed:
            random.seed(seed)
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            new_col = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                new_col.append(cell)   
            self._cells.append(new_col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x_position = self._x1 + i * self._cell_size_x
        y_position = self._y1 + j * self._cell_size_y
        x2 = x_position + self._cell_size_x
        y2 = y_position + self._cell_size_y      
        self._cells[i][j].draw(x_position, y_position, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1,self._num_rows -1)
    

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            need_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                need_visit.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                need_visit.append((i, j - 1))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                need_visit.append((i + 1, j))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                need_visit.append((i, j + 1))
            
            if len(need_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(need_visit))
            next_cell = need_visit[direction]

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
        
            self._break_walls_r(next_cell[0], next_cell[1])
            
    
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = i, j
        self._cells[i][j].visited = True
        
        end_cell = (self._num_cols - 1, self._num_rows - 1) 
        if current_cell == end_cell:
            return True
        #left
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        #right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        #top
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        #bottom
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False
    
    def solve(self):
        return self._solve_r(0, 0)




    
            