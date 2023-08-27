# Write a python program for sparse matrix realization and operations on it- Transpose, 
# Fast Transpose and addition of two matrices 

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = []

    def insert(self, row, col, value):
        self.elements.append((row, col, value))

    def display(self):
        for row in range(self.rows):
            for col in range(self.cols):
                element = 0
                for r, c, v in self.elements:
                    if r == row and c == col:
                        element = v
                        break
                print(element, end="\t")
            print()

    def transpose(self):
        transposed_matrix = SparseMatrix(self.cols, self.rows)
        for r, c, v in self.elements:
            transposed_matrix.insert(c, r, v)
        return transposed_matrix

    def fast_transpose(self):
        row_terms = [0] * self.cols
        starting_pos = [0] * self.cols

        for r, _, _ in self.elements:
            row_terms[r] += 1

        starting_pos[0] = 0
        for i in range(1, self.cols):
            starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1]

        transposed_matrix = SparseMatrix(self.cols, self.rows)
        for r, c, v in self.elements:
            transposed_matrix.insert(c, r, v)
            starting_pos[c] += 1

        return transposed_matrix

    def add_matrices(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_matrix = SparseMatrix(self.rows, self.cols)
        combined_elements = self.elements + other_matrix.elements

        for r in range(self.rows):
            for c in range(self.cols):
                total = 0
                for rr, cc, v in combined_elements:
                    if rr == r and cc == c:
                        total += v
                if total != 0:
                    result_matrix.insert(r, c, total)

        return result_matrix


def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = SparseMatrix(rows, cols)
    print("Enter the elements of the matrix:")
    for r in range(rows):
        row_data = list(map(int, input().split()))
        for c, value in enumerate(row_data):
            if value != 0:
                matrix.insert(r, c, value)

    print("Original Matrix:")
    matrix.display()

    transpose_matrix = matrix.transpose()
    print("\nTranspose of the Matrix:")
    transpose_matrix.display()

    fast_transpose_matrix = matrix.fast_transpose()
    print("\nFast Transpose of the Matrix:")
    fast_transpose_matrix.display()

    print("\nEnter another matrix for addition:")
    other_matrix = SparseMatrix(rows, cols)
    print("Enter the elements of the other matrix:")
    for r in range(rows):
        row_data = list(map(int, input().split()))
        for c, value in enumerate(row_data):
            if value != 0:
                other_matrix.insert(r, c, value)

    print("\nSecond Matrix:")
    other_matrix.display()

    addition_result = matrix.add_matrices(other_matrix)
    print("\nAddition of the two matrices:")
    addition_result.display()


if __name__ == "__main__":
    main()
