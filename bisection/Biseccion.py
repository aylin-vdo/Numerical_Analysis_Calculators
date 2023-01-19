#from stringprep import in_table_a1
#from telnetlib import XAUTH
import tkinter as tk
#from tkinter import *
import customtkinter as ctk
from math import *

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    WIDTH = 1000
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title("Método de la bisección")
        self.resizable(0,0)
        self.iconbitmap("logo.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Recuadros
        self.grid_columnconfigure(4, weight=1)  # cinco columnas
        self.grid_rowconfigure(5, weight=1) #seis filas

        #------Recuadro que contiene opciones------#
        self.recuadro_op = ctk.CTkFrame(master=self, width=300, corner_radius=0, fg_color="#3B8ED0")
        self.recuadro_op.grid(row=0, column=0, sticky="nsew", rowspan=2, columnspan=5)

        #titulo
        self.titulo_op = ctk.CTkLabel(master=self.recuadro_op,
                                              text="Método de la bisección",
                                              text_font=("STXihei", -30),
                                              text_color="white")
        self.titulo_op.grid(row=0, column=0, pady=60, padx=60, columnspan=3)

        #------Recuadro que contiene a procedimiento------#
        self.recuadro_sol = ctk.CTkFrame(master=self)
        self.recuadro_sol.grid(row=2, column=0, sticky="nswe", padx=20, pady=20, rowspan=4, columnspan=5)

        #Botones
        self.IngresarBTN = ctk.CTkButton(master=self.recuadro_sol,text="Ingresar", text_color="white", command=self.biseccion)
        self.IngresarBTN.grid(row=0, column=3, padx=70, pady=5)
        self.IngresarBTN.place(relx=.86, rely=.1, anchor="c")
        self.LimpiarBTN = ctk.CTkButton(master=self.recuadro_sol,text="Limpiar", text_color="white", command=self.limpiar)
        self.LimpiarBTN.place(relx=.45, rely=.70)
        
        #Nombre
        self.ec = ctk.CTkLabel(master=self.recuadro_op,
                                                   text="Aylin V. Demetci Ortiz" ,
                                                   text_color="white"
                                                )
        self.ec.grid(row=0, column=0, sticky="nwe", padx=5, pady=5)

        self.entry1 = ctk.CTkEntry(master=self.recuadro_sol, width=150, placeholder_text="f(x)", corner_radius=4, border_width=1.5, validate='all')
        self.entry1.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry1.place(relx=.2, rely=.1, anchor="c")
        self.entry2 = ctk.CTkEntry(master=self.recuadro_sol, width=50, placeholder_text="xi", corner_radius=4, border_width=1.5, validate='all', )
        self.entry2.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry2.place(relx=.44, rely=.1, anchor="c")
        self.entry3 = ctk.CTkEntry(master=self.recuadro_sol, width=50, placeholder_text="xu", corner_radius=4, border_width=1.5, validate='all')
        self.entry3.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry3.place(relx=.58, rely=.1, anchor="c")
        self.entry4 = ctk.CTkEntry(master=self.recuadro_sol, width=50, placeholder_text="5%", corner_radius=4, border_width=1.5, validate='all')
        self.entry4.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry4.place(relx=.72, rely=.1, anchor="c")

        self.solucion = ctk.CTkLabel(master=self.recuadro_sol,
                                                   text="Sol:\t\t\t\tError:",
                                                   height=200,
                                                   width=800,
                                                   corner_radius=6,
                                                   fg_color="#EBEBEC",
                                                   justify=tk.LEFT,
                                                   text_font=("Default", -16),
                                                   text_color="#7a8287",
                                                   padx=50, pady=50)
        self.solucion.place(relx=.50, rely=.4, anchor="c")

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

    def f(self,x):
        eq = self.entry1.get()
        eq = eq.replace("^", "**" )
        return eval(eq)
    
    def biseccion(self):
        self.xi = float(self.entry2.get())
        self.xu = float(self.entry3.get())
        str1 = self.entry4.get()
        if "%" in str1:
            str1 = str1.replace("%", "")
            self.error = (float(str1))/100
        else:
            self.error = float(self.entry4.get())
        xr2=self.xi
        xr=self.xu
        k=0
        if(self.f(self.xi)*self.f(self.xu)>0):
            print("la funcion no cambia de signo")
        while(abs(xr2-xr)>self.error):
            xr2=xr
            xr=(self.xi+self.xu)/2
            if(self.f(self.xi)*self.f(xr)<0):
                self.xu = xr
            if(self.f(xr)*self.f(self.xu)<0):
                self.xi = xr
            print("intervalo: [",self.xi,",",self.xu,"]")
            k=k+1
        print(" ",xr," es la solucion, con un error de ")
        self.solucion.configure(text="Sol: x = "+str(xr)+"\t\t\tError: "+str((abs(xr2-xr))*100)+"%")

    def limpiar(self):
        self.xi = 0,
        self.xu = 0,
        self.error = 0,
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        self.entry4.delete(0,'end')
        self.solucion.configure(text="Sol:\t\t\t\tError:")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()