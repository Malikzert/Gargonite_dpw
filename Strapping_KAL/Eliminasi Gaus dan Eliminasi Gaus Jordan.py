import tkinter as tk

def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        divisor = matrix[i][i]
        if divisor == 0:
            continue
        for j in range(i, n+1):
            matrix[i][j] /= divisor
        for j in range(i+1, n):
            multiplier = matrix[j][i]
            for k in range(i, n+1):
                matrix[j][k] -= multiplier * matrix[i][k]
    return [row[-1] for row in matrix]

def gauss_jordan_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        divisor = matrix[i][i]
        if divisor == 0:
            continue
        for j in range(i, n+1):
            matrix[i][j] /= divisor
        for j in range(n):
            if j != i:
                multiplier = matrix[j][i]
                for k in range(i, n+1):
                    matrix[j][k] -= multiplier * matrix[i][k]

    return [row[-1] for row in matrix]

def solve():
    matrix = []
    for i in range(3):
        row = []
        for j in range(4):
            entry = float(entries[(i, j)].get())
            row.append(entry)
        matrix.append(row)

    if elimination_choice.get() == 1:
        hasil = gauss_elimination(matrix)
    else:
        hasil = gauss_jordan_elimination(matrix)

    for i in range(3):
        result_label = tk.Label(root, text=f"x{i+1}: {hasil[i]}")
        result_label.grid(row=i+1, column=5)

# Buat GUI
root = tk.Tk()
root.title("Gauss Elimination")

elimination_choice = tk.IntVar()
gauss_radio = tk.Radiobutton(root, text="Gauss Elimination", variable=elimination_choice, value=1)
gauss_radio.grid(row=0, column=4)
gauss_jordan_radio = tk.Radiobutton(root, text="Gauss-Jordan Elimination", variable=elimination_choice, value=2)
gauss_jordan_radio.grid(row=1, column=4)

entries = {}
for i in range(3):
    for j in range(4):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j)
        entries[(i, j)] = entry

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=3, column=3)

root.mainloop()
