import tkinter as tk
from tkinter import messagebox

def create_matrix(entry_widgets, rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(entry_widgets[i][j].get()))
        matrix.append(row)
    return matrix

def display_result(matrix, result_label):
    result = "\n".join(["\t".join(map(str, row)) for row in matrix])
    result_label.config(text=result)

def add_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def subtract_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def multiply_matrices(matrix_a, matrix_b):
    return [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b))) for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

def perform_operation():
    try:
        matrix_a = create_matrix(entry_matrix_a, rows_a, cols_a)
        matrix_b = create_matrix(entry_matrix_b, rows_b, cols_b)
        operation = operation_var.get()
    
        if operation == 'Penjumlahan':
            if rows_a != rows_b or cols_a != cols_b:
                raise ValueError("Kedua matriks harus memiliki dimensi yang sama untuk penjumlahan.")
            result_matrix = add_matrices(matrix_a, matrix_b)
        elif operation == 'Pengurangan':
            if rows_a != rows_b or cols_a != cols_b:
                raise ValueError("Kedua matriks harus memiliki dimensi yang sama untuk pengurangan.")
            result_matrix = subtract_matrices(matrix_a, matrix_b)
        elif operation == 'Perkalian':
            if cols_a != rows_b:
                raise ValueError("Jumlah kolom di Matriks A harus sama dengan jumlah baris di Matriks B untuk perkalian.")
            result_matrix = multiply_matrices(matrix_a, matrix_b)
        
        display_result(result_matrix, result_label)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def generate_entries():
    global entry_matrix_a, entry_matrix_b, rows_a, cols_a, rows_b, cols_b

    rows_a = int(entry_rows_a.get())
    cols_a = int(entry_cols_a.get())
    rows_b = int(entry_rows_b.get())
    cols_b = int(entry_cols_b.get())

    for widget in entry_frame.winfo_children():
        widget.grid_forget()

    entry_matrix_a = []
    entry_matrix_b = []

    tk.Label(entry_frame, text="Matriks A").grid(row=2, column=0, columnspan=cols_a, pady=5)
    for i in range(rows_a):
        row_a = []
        for j in range(cols_a):
            entry_a = tk.Entry(entry_frame, width=5)
            entry_a.grid(row=i+3, column=j, padx=5, pady=5)
            row_a.append(entry_a)
        entry_matrix_a.append(row_a)

    tk.Label(entry_frame, text="Matriks B").grid(row=2, column=cols_a+2, columnspan=cols_b, pady=5)
    for i in range(rows_b):
        row_b = []
        for j in range(cols_b):
            entry_b = tk.Entry(entry_frame, width=5)
            entry_b.grid(row=i+3, column=j+cols_a+2, padx=5, pady=5)
            row_b.append(entry_b)
        entry_matrix_b.append(row_b)

app = tk.Tk()
app.title("Operasi Matriks")

# Initial setup to get matrix order
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Baris A:").grid(row=0, column=0)
entry_rows_a = tk.Entry(input_frame, width=5)
entry_rows_a.grid(row=0, column=1)

tk.Label(input_frame, text="Kolom A:").grid(row=0, column=2)
entry_cols_a = tk.Entry(input_frame, width=5)
entry_cols_a.grid(row=0, column=3)

tk.Label(input_frame, text="Baris B:").grid(row=1, column=0)
entry_rows_b = tk.Entry(input_frame, width=5)
entry_rows_b.grid(row=1, column=1)

tk.Label(input_frame, text="Kolom B:").grid(row=1, column=2)
entry_cols_b = tk.Entry(input_frame, width=5)
entry_cols_b.grid(row=1, column=3)

btn_generate = tk.Button(input_frame, text="Buat Matriks", command=generate_entries)
btn_generate.grid(row=2, columnspan=4)

entry_frame = tk.Frame(app)
entry_frame.pack(pady=10)

operation_frame = tk.Frame(app)
operation_frame.pack(pady=10)

operation_var = tk.StringVar(value='Penjumlahan')
operation_label = tk.Label(operation_frame, text="Pilih Operasi:")
operation_label.grid(row=0, column=0)
add_radiobutton = tk.Radiobutton(operation_frame, text="Penjumlahan", variable=operation_var, value='Penjumlahan')
add_radiobutton.grid(row=0, column=1)
subtract_radiobutton = tk.Radiobutton(operation_frame, text="Pengurangan", variable=operation_var, value='Pengurangan')
subtract_radiobutton.grid(row=0, column=2)
multiply_radiobutton = tk.Radiobutton(operation_frame, text="Perkalian", variable=operation_var, value='Perkalian')
multiply_radiobutton.grid(row=0, column=3)

btn_calculate = tk.Button(operation_frame, text="Hitung", command=perform_operation)
btn_calculate.grid(row=1, column=0, columnspan=4)

result_label = tk.Label(app, text="", justify=tk.LEFT)
result_label.pack(pady=10)

app.mainloop()
