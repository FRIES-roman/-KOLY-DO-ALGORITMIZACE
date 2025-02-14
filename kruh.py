import tkinter as tk

root = tk.Tk()
root.title("Kreslení kruhu")

canvas = tk.Canvas(root, width=500, height=500, bg='white')
canvas.pack()

canvas.create_oval(100, 100, 300, 300, outline='red', width=2)

root.mainloop()
