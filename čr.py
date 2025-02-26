import tkinter as tk


FLAG_WIDTH = 300  
FLAG_HEIGHT = 200  
root = tk.Tk()
root.title("Vlajka České republiky")

canvas = tk.Canvas(root, width=FLAG_WIDTH, height=FLAG_HEIGHT, bg='white')
canvas.pack()

canvas.create_rectangle(0, FLAG_HEIGHT/2, FLAG_WIDTH, FLAG_HEIGHT, fill='red', outline='')

canvas.create_polygon(0, 0, 0, FLAG_HEIGHT, FLAG_WIDTH/2, FLAG_HEIGHT/2, fill='blue', outline='')

root.mainloop()