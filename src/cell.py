from graphics import Line, Point, Circle
class Cell:
    def __init__(self, win = None):
       self.has_circle = False
       self.has_top_wall = True
       self.has_right_wall = True
       self.has_bottom_wall = True
       self.has_left_wall = True
       self._x1 = None
       self._y1 = None
       self._x2 = None
       self._y2 = None
       self._win = win
       self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_circle:
            circle = Circle(Point((x1 + x2)/2, (y1 + y2)/2), r = min((x2 - x1)/2, (y2 - y1)/2))
            self._win.draw_circle(circle)
    
    def draw_move(self, to_cell, undo=False):
        origin_x = (self._x1 + self._x2)/2
        origin_y = (self._y1 + self._y2)/2
        target_x = (to_cell._x1 + to_cell._x2)/2
        target_y = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(origin_x, origin_y), Point(target_x, target_y))
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)
