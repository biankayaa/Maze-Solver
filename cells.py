from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    
    def draw_move(self, to_cell, undo=False):
        half_self = abs(self._x2 - self._x1)//2
        x_centered_self = half_self + self._x1
        y_centered_self = half_self + self._y1

        half_to_cell = abs(to_cell._x2 -to_cell._x1)//2
        x_centered_tc = half_to_cell + to_cell._x1
        y_centered_tc = half_to_cell + to_cell._y1

        fill_color = "gray" if undo else "red"

        line = Line(Point(x_centered_self, y_centered_self), Point(x_centered_tc, y_centered_tc))
        self._win.draw_line(line, fill_color) 


    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")
    

             
                








