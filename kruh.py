import tkinter as tk


root = tk.Tk()
root.title("Mezikružné kružnice")


canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()


x1, y1 = 50, 50  
x2, y2 = 450, 450  
step = 20  

for i in range(10): 
    if i % 2 == 0:  
        color = "red"
    else:  
        color = "blue"
    
    canvas.create_oval(x1, y1, x2, y2, outline=color, width=3)
    x1 += step  
    y1 += step
    x2 -= step  
    y2 -= step

root.mainloop()
