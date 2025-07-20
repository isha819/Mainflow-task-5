def rotate_matrix(matrix):
    # Transpose the matrix
    transposed = list(zip(*matrix))
    # Reverse each row
    rotated = [list(row)[::-1] for row in transposed]
    return rotated

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print(f"Enter the matrix row by row (each row with {cols} space-separated integers):")
matrix = []
for i in range(rows):
    row = list(map(int, input().strip().split()))
    if len(row) != cols:
        print("Invalid row length! Try again.")
        exit()
    matrix.append(row)

rotated = rotate_matrix(matrix)

print("Rotated matrix (90 degrees clockwise):")
for row in rotated:
    print(*row)
