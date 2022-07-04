# usar * para importar todo es una mala practica
from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, padding=20)
frame.grid()

# para que aparezca el texto que queramos necesitamos hacer un label y un pack para que aparezca en pantalla. Hay multitud de parametros que le podemos dar como color, borde, tamaño....(DEFINICION)
label_one = Label(frame, text="Hello TKinter", padx=50, pady= 25, bg = "white")
# con el grid posicionamos las etiquetas en las filas y columnas que queramos. Tienen que ser labels consecutivos para que se vea.(SITUACION)
label_one.grid(row=0, column=0)

label_two = Label(frame, text="I'm another label", fg="yellow", bg="#333333", padx=100)
label_two.grid(row=5, column=0, columnspan=4)

label_three = Label(frame, text="", padx=50, pady=50)
label_three.grid(row=3, column=2)

label_four = Button(frame, text="Click me!!")
label_four.grid(row=2, column=1)



root.mainloop()