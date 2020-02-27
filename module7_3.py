class Cells:

    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __add__(self, other):
        return self.num_of_cells + other

    def __sub__(self, other):
        return self.num_of_cells - other

    def __mul__(self, other):
        return self.num_of_cells * other

    def __truediv__(self, other):
        return round(self.num_of_cells / other)

    def make_order(self, cell_in_row):
        self.celling = ""
        while self.num_of_cells > 0:
            self.num_of_cells -= cell_in_row
            if self.num_of_cells < 0:
                self.celling += ("*" * (cell_in_row + self.num_of_cells) + "\n")
            else:
                self.celling += ("*" * cell_in_row + "\n")
        return self.celling

    def __call__(self, new_num_of_cells):
        self.num_of_cells = new_num_of_cells

cell = Cells(24)
print(cell.make_order(6))