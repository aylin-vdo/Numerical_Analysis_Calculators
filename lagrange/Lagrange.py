import tkinter as tk
#from tkinter import *
import customtkinter as ctk
from math import *
from PIL import ImageTk, Image
from array import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("UI_sources\darkgreen.json")

class App(ctk.CTk):

    WIDTH = 1000
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title("")
        self.resizable(0,0)
        self.iconbitmap("UI_sources\logo.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Recuadros
        self.grid_columnconfigure(4, weight=1)  # cinco columnas
        self.grid_rowconfigure(5, weight=1) #seis filas

        #------Recuadro que contiene opciones------#
        self.recuadro_op = ctk.CTkFrame(master=self, width=300, corner_radius=0, fg_color="#3C8000")
        self.recuadro_op.grid(row=0, column=0, sticky="nsew", rowspan=2, columnspan=5)

        #titulo
        self.titulo_op = ctk.CTkLabel(master=self.recuadro_op,
                                              text="Método de Lagrange",
                                              text_font=("FZYaoTi", -50),
                                              text_color="white"
                                              )
        self.titulo_op.grid(row=0, column=0, pady=60, padx=60, columnspan=3)

        #------Recuadro que contiene a procedimiento------#
        self.recuadro_sol = ctk.CTkFrame(master=self, fg_color="#000000")
        self.recuadro_sol.grid(row=2, column=0, sticky="nswe", padx=0, pady=0, rowspan=4, columnspan=5)
        
        img = Image.open("UI_sources\caja.png").resize((2000, 1600))
        self.bg_img = ImageTk.PhotoImage(img)
        self.IMGdisplay = tk.Label(master=self.recuadro_sol, image = self.bg_img)
        self.IMGdisplay.place(relx=-.001, rely=-.01)       
        
        self.IngresarBTN = ctk.CTkButton(master=self.recuadro_sol,text="Ingresar",text_font=("FZYaoTi", -20), text_color="white", command=self.lagrange)
        self.IngresarBTN.place(relx=.32, rely=.3)

        self.LimpiarBTN = ctk.CTkButton(master=self.recuadro_sol,text="Limpiar", text_font=("FZYaoTi", -20), text_color="white", command=self.limpiar)
        self.LimpiarBTN.place(relx=.5, rely=.3)

        self.ex = ctk.CTkLabel(master=self.recuadro_sol, text="Ingresar valores de x, e.g. [x1, x2, x3]" , text_font=("FZYaoTi", -20), text_color="white")
        self.ex.place(relx=.04, rely=.1)
        self.ex2 = ctk.CTkLabel(master=self.recuadro_sol, text="e.g. [y1, y2, y3]" , text_font=("FZYaoTi", -20), text_color="white")
        self.ex2.place(relx=.4, rely=.1)
        self.ex3 = ctk.CTkLabel(master=self.recuadro_sol, text="Cantidad de puntos" , text_font=("FZYaoTi", -20), text_color="white")
        self.ex3.place(relx=.6, rely=.1)
        self.ex4 = ctk.CTkLabel(master=self.recuadro_sol, text="Punto de interpolacion" , text_font=("FZYaoTi", -20), text_color="white")
        self.ex4.place(relx=.8, rely=.1)

        self.entry1 = ctk.CTkEntry(master=self.recuadro_sol ,width=200 ,placeholder_text="x1 x2 x3",text_font=("FZYaoTi", -20) ,corner_radius=4, border_width=1.5)
        self.entry1.place(relx=.14, rely=.2, anchor="c")
        self.entry2 = ctk.CTkEntry(master=self.recuadro_sol ,width=200 ,placeholder_text="y1 y2 y3",text_font=("FZYaoTi", -20) ,corner_radius=4, border_width=1.5)
        self.entry2.place(relx=.47, rely=.2, anchor="c")
        self.entry3 = ctk.CTkEntry(master=self.recuadro_sol ,width=100 ,placeholder_text="n",text_font=("FZYaoTi", -20) ,corner_radius=4, border_width=1.5)
        self.entry3.place(relx=.67, rely=.2, anchor="c")
        self.entry4 = ctk.CTkEntry(master=self.recuadro_sol ,width=100 ,placeholder_text="z",text_font=("FZYaoTi", -20) ,corner_radius=4, border_width=1.5)
        self.entry4.place(relx=.87, rely=.2, anchor="c")

        self.sol = ctk.CTkLabel(master=self.recuadro_sol, text="Solucion: " , text_font=("FZYaoTi", -25), text_color="white")
        self.sol.place(relx=.1, rely=.5)

        #Nombre
        self.nom = ctk.CTkLabel(master=self.recuadro_op, text="Aylin V. Demetci Ortiz", text_font=("FZYaoTi", -20), text_color="white")
        self.nom.place(relx=.1, rely=.1)


    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()
    
    def lagrange(self):
        inputX = self.entry1.get()
        inputY = self.entry2.get()
        n = int(self.entry3.get())
        z = float(self.entry4.get())
        x = array('f',(float(i) for i in inputX.split(",")))
        y = array('f',(float(i) for i in inputY.split(",")))
        if (self.entry1.get())!="":
            solution = 0
            for i in range(n):
                temp = 1
                for j in range(n):
                    if i != j:
                        temp = temp * (z - x[j])/(x[i] - x[j])
                solution = solution + temp * y[i]    
            self.sol.configure(text="El valor interpolado en %.3f es %.3f" % (z, solution))

    def limpiar(self):
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        self.entry4.delete(0,'end')
        self.sol.configure(text="Solucion: ")

if __name__ == "__main__":
    app = App()
    app.mainloop()