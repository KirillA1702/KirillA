
A = [
    [31, 22],
    [37, 43],
    [51, 86]
]
B = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]
]
C = [
    [3, 5, 8, 3],
    [8, 3, 7, 1]
]



class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        return Matrix(list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)), self.matrix, other.matrix)))

a = Matrix(A)
b = Matrix(B)
c = Matrix(C)

print(a + b); print('=' * 10)
print(b + c); print('=' * 10)
print(c + a)