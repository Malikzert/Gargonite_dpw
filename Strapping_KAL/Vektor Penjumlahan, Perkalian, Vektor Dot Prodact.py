import tkinter as tk
from tkinter import messagebox
import math

def penjumlahan_vektor(vektor1, vektor2):
    if len(vektor1) != len(vektor2):
        return "Panjang kedua vektor harus sama"
    hasil = []
    for i in range(len(vektor1)):
        hasil.append(vektor1[i] + vektor2[i])
    return hasil

def pengurangan_vektor(vektor1, vektor2):
    if len(vektor1) != len(vektor2):
        return "Panjang kedua vektor harus sama"
    hasil = []
    for i in range(len(vektor1)):
        hasil.append(vektor1[i] - vektor2[i])
    return hasil

def perkalian_vektor(vektor1, vektor2):
    if len(vektor1) != len(vektor2):
        return "Panjang kedua vektor harus sama"
    hasil = []
    for i in range(len(vektor1)):
        hasil.append(vektor1[i] * vektor2[i])
    return hasil

def dot_product(vektor1, vektor2, sudut_elevasi):
    if len(vektor1) != len(vektor2):
        return "Error: Panjang vektor tidak sama"
    if sudut_elevasi == None:
        hasil = 0
        for i in range(len(vektor1)):
            hasil += vektor1[i] * vektor2[i]
        return hasil
    else:
        sudut_radian = math.radians(sudut_elevasi)
        hasil = 0
        for i in range(len(vektor1)):
            hasil += vektor1[i] * vektor2[i] * math.cos(sudut_radian)
        return hasil

def hitung():
    try:
        vektor1 = [float(x) for x in entry_vektor1.get().split(",")]
        vektor2 = [float(x) for x in entry_vektor2.get().split(",")]
        sudut_elevasi = float(entry_sudut.get())
        
        if operasi.get() == 1:
            hasil = penjumlahan_vektor(vektor1, vektor2)
        elif operasi.get() == 2:
            hasil = pengurangan_vektor(vektor1, vektor2)
        elif operasi.get() == 3:
            hasil = perkalian_vektor(vektor1, vektor2)
        else:
            hasil = dot_product(vektor1, vektor2, sudut_elevasi)
        
        messagebox.showinfo("Hasil Perhitungan", f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator Vektor")

label_vektor1 = tk.Label(root, text="Vektor 1 (pisahkan dengan koma):")
label_vektor1.pack()
entry_vektor1 = tk.Entry(root)
entry_vektor1.pack()

label_vektor2 = tk.Label(root, text="Vektor 2 (pisahkan dengan koma):")
label_vektor2.pack()
entry_vektor2 = tk.Entry(root)
entry_vektor2.pack()

label_sudut = tk.Label(root, text="Sudut Elevasi (dalam derajat):")
label_sudut.pack()
entry_sudut = tk.Entry(root)
entry_sudut.pack()

operasi = tk.IntVar()
operasi.set(4)

radiobutton_penjumlahan = tk.Radiobutton(root, text="Penjumlahan", variable=operasi, value=1)
radiobutton_penjumlahan.pack()
radiobutton_pengurangan = tk.Radiobutton(root, text="Pengurangan", variable=operasi, value=2)
radiobutton_pengurangan.pack()
radiobutton_perkalian = tk.Radiobutton(root, text="Perkalian", variable=operasi, value=3)
radiobutton_perkalian.pack()
radiobutton_dot_product = tk.Radiobutton(root, text="Dot Product", variable=operasi, value=4)
radiobutton_dot_product.pack()

button_hitung = tk.Button(root, text="Hitung", command=hitung)
button_hitung.pack()

root.mainloop()
