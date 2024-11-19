class Matrix:
    def __init__(self, rows, cols, fill=0):
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def update(self, row, col, value):
        self.data[row][col] = value

    def access(self, row, col):
        return self.data[row][col]

    def delete_row(self, row):
        if row >= len(self.data) or row < 0:
            raise IndexError("Row out of range")
        self.data.pop(row)
