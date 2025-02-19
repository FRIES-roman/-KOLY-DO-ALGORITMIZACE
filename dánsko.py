import tkinter as tk


FLAG_WIDTH = 340  
FLAG_HEIGHT = 280  


root = tk.Tk()
root.title("Vlajka Dánska")


canvas = tk.Canvas(root, width=FLAG_WIDTH, height=FLAG_HEIGHT, bg='red')
canvas.pack()

cross_vertical_x = FLAG_WIDTH * (12 / 34)  
cross_horizontal_y = FLAG_HEIGHT * (12 / 28) 


canvas.create_rectangle(cross_vertical_x, 0, cross_vertical_x + (FLAG_WIDTH / 7), FLAG_HEIGHT, fill='white', outline='')


canvas.create_rectangle(0, cross_horizontal_y, FLAG_WIDTH, cross_horizontal_y + (FLAG_HEIGHT / 7), fill='white', outline='')

root.mainloop()
