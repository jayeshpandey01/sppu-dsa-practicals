# Write a python program that determines the location of a saddle point of matrix if one 
# exists. An m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest 
# value in row i and the largest value in j. 

def find_saddle_point(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        min_in_row = min(matrix[i])
        min_index = matrix[i].index(min_in_row)
        
        is_saddle_point = True
        for j in range(rows):
            if matrix[j][min_index] > min_in_row:
                is_saddle_point = False
                break
        
        if is_saddle_point:
            return (i, min_index)
    
    return None

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (separated by spaces): ").split()))
        matrix.append(row)
    
    saddle_point = find_saddle_point(matrix)
    
    if saddle_point:
        row, col = saddle_point
        print(f"Saddle point found at location ({row}, {col}) with value {matrix[row][col]}.")
    else:
        print("No saddle point found in the matrix.")

if __name__ == "__main__":
    main()
