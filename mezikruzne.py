import tkinter as tk

# Inicializace okna
root = tk.Tk()
root.title("Mezikružné kružnice")

# Vytvoření plátna
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Počáteční hodnoty
x1, y1 = 50, 50  # Souřadnice levého horního rohu
x2, y2 = 450, 450  # Souřadnice pravého dolního rohu
step = 20  # Krok zmenšení

# Kreslení mezikruží pomocí cyklu
for i in range(10):  # 10 mezikruží
    if i % 2 == 0:  # Každé sudé mezikruží bude červené
        color = "red"
    else:  # Každé liché mezikruží bude modré
        color = "blue"
    
    canvas.create_oval(x1, y1, x2, y2, outline=color, width=3)
    x1 += step  # Zmenšení levého horního rohu
    y1 += step
    x2 -= step  # Zmenšení pravého dolního rohu
    y2 -= step

root.mainloop()