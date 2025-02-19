import tkinter as tk

# Konstanty pro velikost vlajky
FLAG_WIDTH = 300  # Šířka
FLAG_HEIGHT = 200  # Výška (2:3 poměr)

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Vlajka České republiky")

# Vytvoření kreslící plochy (Canvas)
canvas = tk.Canvas(root, width=FLAG_WIDTH, height=FLAG_HEIGHT, bg='white')
canvas.pack()

# Červený spodní obdélník
canvas.create_rectangle(0, FLAG_HEIGHT/2, FLAG_WIDTH, FLAG_HEIGHT, fill='red', outline='')

# Modrý trojúhelník
canvas.create_polygon(0, 0, 0, FLAG_HEIGHT, FLAG_WIDTH/2, FLAG_HEIGHT/2, fill='blue', outline='')

# Spuštění hlavní smyčky
root.mainloop()