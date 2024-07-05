import tkinter as tk
from tkinter import messagebox
import re

def cek_persamaan():
    persamaan = entry_persamaan.get()
    if '=' in persamaan:
        messagebox.showinfo("Hasil", "Merupakan Persamaan Linier")
        hitung_variabel(persamaan)
    elif any(op in persamaan for op in ['<', '>', '≤', '≥', '^', '√']):
        messagebox.showinfo("Hasil", "Merupakan Pertidaksamaan Linier")
        hitung_variabel_pertidaksamaan(persamaan)
    else:
        messagebox.showinfo("Hasil", "Tidak dapat menentukan, masukkan persamaan dengan benar")

def hitung_variabel(persamaan):
    variabel_set = set()
    variabel_koefisien = {}
    konstanta = None
    
    angka_pattern = r'[-+]?\d*\.\d+|[-+]?\d+'
    splitted = persamaan.split('=')
    if len(splitted) == 2:
        sisi_kiri, sisi_kanan = splitted
        for char in sisi_kiri:
            if char.isalpha():
                variabel_set.add(char)
        koefisiens = re.findall(angka_pattern, sisi_kiri)
        for i, var in enumerate(variabel_set):
            variabel_koefisien[var] = float(koefisiens[i]) if i < len(koefisiens) else 0.0
        konstanta = float(sisi_kanan.strip())
    
    messagebox.showinfo("Jumlah Variabel", f"Jumlah variabel dalam persamaan adalah {len(variabel_set)}")
    messagebox.showinfo("Koefisien", f"Koefisien dalam persamaan adalah {variabel_koefisien}")
    messagebox.showinfo("Konstanta", f"Konstanta dalam persamaan adalah {konstanta}")

def hitung_variabel_pertidaksamaan(pertidaksamaan):
    variabel_set = set()
    variabel_koefisien = {}
    konstanta = None
    
    angka_pattern = r'[-+]?\d*\.\d+|[-+]?\d+'
    for op in ['<', '>', '≤', '≥']:
        if op in pertidaksamaan:
            splitted = pertidaksamaan.split(op)
            sisi_kiri, sisi_kanan = splitted[0], splitted[1]
            break
    
    for char in sisi_kiri:
        if char.isalpha():
            variabel_set.add(char)
    koefisiens = re.findall(angka_pattern, sisi_kiri)
    for i, var in enumerate(variabel_set):
        variabel_koefisien[var] = float(koefisiens[i]) if i < len(koefisiens) else 0.0
    konstanta = float(sisi_kanan.strip())
    
    messagebox.showinfo("Jumlah Variabel", f"Jumlah variabel dalam pertidaksamaan adalah {len(variabel_set)}")
    messagebox.showinfo("Koefisien", f"Koefisien dalam pertidaksamaan adalah {variabel_koefisien}")
    messagebox.showinfo("Konstanta", f"Konstanta dalam pertidaksamaan adalah {konstanta}")


root = tk.Tk()
root.title("Cek Persamaan")

label = tk.Label(root, text="Masukkan Persamaan:")
label.pack()

entry_persamaan = tk.Entry(root, width=30)
entry_persamaan.pack()

tombol_cek = tk.Button(root, text="Cek", command=cek_persamaan)
tombol_cek.pack()

contoh_label = tk.Label(root, text="Contoh: x + 2y =0 atau x + 3y + 2z ≥ 0")
contoh_label.pack()

root.mainloop()
