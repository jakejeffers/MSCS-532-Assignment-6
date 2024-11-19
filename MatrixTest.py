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
# Testing the Matrix class
matrix = Matrix(3, 3, fill=0)  # 3x3 matrix filled with 0
matrix.update(1, 1, 5)  # Set matrix[1][1] to 5
print("Matrix after update:")
for row in matrix.data:
    print(row)

matrix.delete_row(1)  # Remove the second row
print("Matrix after row deletion:")
for row in matrix.data:
    print(row)
