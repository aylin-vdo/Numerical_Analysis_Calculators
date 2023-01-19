import tkinter
import customtkinter
import numpy as np

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title("Montante - Aylin Demetci")
        self.resizable(0,0)
        self.iconbitmap("logo.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        vcmd = (self.register(self.callback))

        self.inv = 'false'
        self.m = np.zeros((9), dtype=int)
        self.a = np.zeros((9), dtype=int)
        self.m_inv = np.zeros((9), dtype=float)

        #Recuadros
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

                    #------Recuadro que contiene opciones------#

        self.recuadro_op = customtkinter.CTkFrame(master=self, width=300, corner_radius=0)
        self.recuadro_op.grid(row=0, column=1, sticky="nswe")
        
        #titulo
        self.titulo_op = customtkinter.CTkLabel(master=self.recuadro_op,
                                              text="Método Montante",
                                              text_font=("Roboto Medium", -30))
        self.titulo_op.grid(row=1, column=1, pady=40, padx=40)

        #Texto ecuaciones
        self.ec = customtkinter.CTkLabel(master=self.recuadro_op,
                                                   text="\nx1  +\t       x2  +\t             x3  = \n\n"+
                                                        "\nx1  +\t       x2  +\t             x3  = \n\n"+
                                                        "\nx1  +\t       x2  +\t             x3  = \n\n" ,
                                                )
        self.ec.grid(row=2, column=1, sticky="nwe", padx=15, pady=15)
        self.ec.place(anchor="c", relx=.46, rely=.25)

        #Entrada Ec. 1

        self.entry1 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry1.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry1.place(relx=.096, rely=.18, anchor="c")
        self.entry2 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry2.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry2.place(relx=.34, rely=.18, anchor="c")
        self.entry3 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry3.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry3.place(relx=.58, rely=.18, anchor="c")
        self.entry4 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry4.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry4.place(relx=.83, rely=.18, anchor="c")

        #Entrada Ec. 2

        self.entry5 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry5.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry5.place(relx=.096, rely=.24, anchor="c")
        self.entry6 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry6.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry6.place(relx=.34, rely=.24, anchor="c")
        self.entry7 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry7.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry7.place(relx=.58, rely=.24, anchor="c")
        self.entry8 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry8.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry8.place(relx=.83, rely=.24, anchor="c")

        #Entrada Ec. 3

        self.entry9 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry9.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry9.place(relx=.096, rely=.3, anchor="c")
        self.entry10 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry10.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry10.place(relx=.34, rely=.3, anchor="c")
        self.entry11 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry11.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry11.place(relx=.58, rely=.3, anchor="c")
        self.entry12 = customtkinter.CTkEntry(master=self.recuadro_op, width=35,placeholder_text="0", corner_radius=4,border_width=1.5, validate='all', validatecommand=(vcmd, '%P'))
        self.entry12.grid(row=2, column=1, pady=20, padx=20, sticky="we")
        self.entry12.place(relx=.83, rely=.3, anchor="c")

        #Botones
        self.IngresarBTN = customtkinter.CTkButton(master=self.recuadro_op,text="Ingresar",command=self.traerEntradas)
        self.IngresarBTN.place(relx=.5, rely=.4, anchor="c")
        self.LimpiarBTN = customtkinter.CTkButton(master=self.recuadro_op,text="Limpiar",command=self.limpiarEntradas)
        self.LimpiarBTN.place(relx=.5, rely=.45, anchor="c")
        self.InversaBTN = customtkinter.CTkButton(master=self.recuadro_op,text="Inversa",command=self.traerInversa)
        self.InversaBTN.place(relx=.5, rely=.50, anchor="c")

        #Nombre
        self.ec = customtkinter.CTkLabel(master=self.recuadro_op,
                                                   text="Aylin V. Demetci Ortiz" ,
                                                )
        self.ec.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.ec.place(anchor="c", relx=.74, rely=.98)


                    #------Recuadro que contiene a matriz------#

        self.recuadro_matriz = customtkinter.CTkFrame(master=self)
        self.recuadro_matriz.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        #fondo gris de matriz
        self.matriz_bg = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.matriz_bg.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.matriz_bg.rowconfigure(0, weight=1)
        self.matriz_bg.columnconfigure(0, weight=1)

        #fondo gris de adjunta
        self.adj_bg = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.adj_bg.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.adj_bg.rowconfigure(0, weight=1)
        self.adj_bg.columnconfigure(0, weight=1)

        #label de matriz
        self.matriz = customtkinter.CTkLabel(master=self.matriz_bg,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.matriz.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.matriz_bg.place(anchor="c", relx=.3, rely=.1)

        #label de adjunta
        self.adj = customtkinter.CTkLabel(master=self.adj_bg,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.adj.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.adj_bg.place(anchor="c", relx=.58, rely=.1)

                    #------Matrices 2, 3, 4------#

        self.matriz_bg1 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.matriz_bg1.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.matriz_bg1.rowconfigure(0, weight=1)
        self.matriz_bg1.columnconfigure(0, weight=1)
        self.adj_bg1 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.adj_bg1.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.adj_bg1.rowconfigure(0, weight=1)
        self.adj_bg1.columnconfigure(0, weight=1)
        self.matriz1 = customtkinter.CTkLabel(master=self.matriz_bg1,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.matriz1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.matriz_bg1.place(anchor="c", relx=.3, rely=.26)
        self.adj1 = customtkinter.CTkLabel(master=self.adj_bg1,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.adj1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.adj_bg1.place(anchor="c", relx=.58, rely=.26)

        self.matriz_bg2 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.matriz_bg2.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.matriz_bg2.rowconfigure(0, weight=1)
        self.matriz_bg2.columnconfigure(0, weight=1)
        self.adj_bg2 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.adj_bg2.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.adj_bg2.rowconfigure(0, weight=1)
        self.adj_bg2.columnconfigure(0, weight=1)
        self.matriz2 = customtkinter.CTkLabel(master=self.matriz_bg2,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.matriz2.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.matriz_bg2.place(anchor="c", relx=.3, rely=.42)
        self.adj2 = customtkinter.CTkLabel(master=self.adj_bg2,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.adj2.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.adj_bg2.place(anchor="c", relx=.58, rely=.42)

        self.matriz_bg3 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.matriz_bg3.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.matriz_bg3.rowconfigure(0, weight=1)
        self.matriz_bg3.columnconfigure(0, weight=1)
        self.adj_bg3 = customtkinter.CTkFrame(master=self.recuadro_matriz)
        self.adj_bg3.grid(row=0, column=1, columnspan=2, rowspan=4, pady=20, padx=20)
        self.adj_bg3.rowconfigure(0, weight=1)
        self.adj_bg3.columnconfigure(0, weight=1)
        self.matriz3 = customtkinter.CTkLabel(master=self.matriz_bg3,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.matriz3.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.matriz_bg3.place(anchor="c", relx=.3, rely=.58)
        self.adj3 = customtkinter.CTkLabel(master=self.adj_bg3,
                                                   text="0\t0\t0\n\n" +
                                                        "0\t0\t0\n\n" +
                                                        "0\t0\t0" ,
                                                )
        self.adj3.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.adj_bg3.place(anchor="c", relx=.58, rely=.58)

        # Linea de proceso
        self.linea = customtkinter.CTkLabel(master=self.recuadro_matriz,
                                            text="~",text_font=("Roboto Medium", -30),width=10)
        self.linea.grid(row=0, column=1, pady=0, padx=0)
        self.linea.place(anchor="c", relx=.1, rely=.26)
        self.linea = customtkinter.CTkLabel(master=self.recuadro_matriz,
                                            text="~",text_font=("Roboto Medium", -30),width=10)
        self.linea.grid(row=0, column=1, pady=0, padx=0)
        self.linea.place(anchor="c", relx=.1, rely=.42)
        self.linea = customtkinter.CTkLabel(master=self.recuadro_matriz,
                                            text="~",text_font=("Roboto Medium", -30),width=10)
        self.linea.grid(row=0, column=1, pady=0, padx=0)
        self.linea.place(anchor="c", relx=.1, rely=.58)

        #Pivotes
        self.piv1 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="pivote ant. = 1\npivote act. =", width=10)
        self.piv1.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.piv1.place(anchor="c", relx=.85, rely=.1)
        self.piv2 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="pivote ant. =\npivote act. =", width=10)
        self.piv2.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.piv2.place(anchor="c", relx=.85, rely=.26)
        self.piv3 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="pivote ant. =\npivote act. =", width=10)
        self.piv3.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.piv3.place(anchor="c", relx=.85, rely=.42)
        
        #Determinante
        self.adjfinal = customtkinter.CTkLabel(master=self.recuadro_matriz,text="Adjunta", width=10)
        self.adjfinal.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.adjfinal.place(anchor="c", relx=.8, rely=.58)
        self.det = customtkinter.CTkLabel(master=self.recuadro_matriz,text="Determinante = ", width=10, height=10)
        self.det.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.det.place(anchor="c", relx=.3, rely=.7)

        #Solucion
        self.solx1 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="x1 = ", width=10, height=10)
        self.solx1.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.solx1.place(anchor="c", relx=.3, rely=.78)
        self.solx2 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="x2 = ", width=10, height=10)
        self.solx2.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.solx2.place(anchor="c", relx=.3, rely=.82)
        self.solx3 = customtkinter.CTkLabel(master=self.recuadro_matriz,text="x3 = ", width=10, height=10)
        self.solx3.grid(row=2, column=1, sticky="nwe", padx=0, pady=0)
        self.solx3.place(anchor="c", relx=.3, rely=.86)

    def button_event(self):
        print("Button pressed")

    def on_closing(self, event=0):
        self.destroy()

#------Funciones para Metodo------#

#Metodo Montante

    def paso1(self):
        self.matriz.configure(text=(str(self.m[0])+"\t"+str(self.m[1])+"\t"+str(self.m[2])+"\n\n" +
                                str(self.m[3])+"\t"+str(self.m[4])+"\t"+str(self.m[5])+"\n\n" +
                                str(self.m[6])+"\t"+str(self.m[7])+"\t"+str(self.m[8])))
        self.adj.configure(text=(str(self.a[0])+"\t"+str(self.a[1])+"\t"+str(self.a[2])+"\n\n" +
                            str(self.a[3])+"\t"+str(self.a[4])+"\t"+str(self.a[5])+"\n\n" +
                            str(self.a[6])+"\t"+str(self.a[7])+"\t"+str(self.a[8])))
        self.piv1.configure(text="pivote ant. = 1\npivote act. = "+str(self.m[0]))
        self.m[4]= (self.m[0]*self.m[4])-(self.m[1]*self.m[3])
        self.m[5]= (self.m[0]*self.m[5])-(self.m[2]*self.m[3])
        self.m[7]= (self.m[0]*self.m[7])-(self.m[1]*self.m[6])
        self.m[8]= (self.m[0]*self.m[8])-(self.m[2]*self.m[6])
        self.a[3]= (self.m[0]*self.a[3])-(self.m[3]*self.a[0])
        self.a[4]= (self.m[0]*self.a[4])-(self.m[3]*self.a[1])
        self.a[5]= (self.m[0]*self.a[5])-(self.m[3]*self.a[2])
        self.a[6]= (self.m[0]*self.a[6])-(self.m[6]*self.a[0])
        self.a[7]= (self.m[0]*self.a[7])-(self.m[6]*self.a[1])
        self.a[8]= (self.m[0]*self.a[8])-(self.m[6]*self.a[2])
        self.m[3]=0
        self.m[6]=0
        self.piv2.configure(text="pivote ant. = "+str(self.m[0])+"\npivote act. = "+str(self.m[4]))
        self.matriz1.configure(text=(str(self.m[0])+"\t"+str(self.m[1])+"\t"+str(self.m[2])+"\n\n" +
                                str(self.m[3])+"\t"+str(self.m[4])+"\t"+str(self.m[5])+"\n\n" +
                                str(self.m[6])+"\t"+str(self.m[7])+"\t"+str(self.m[8])))
        self.adj1.configure(text=(str(self.a[0])+"\t"+str(self.a[1])+"\t"+str(self.a[2])+"\n\n" +
                            str(self.a[3])+"\t"+str(self.a[4])+"\t"+str(self.a[5])+"\n\n" +
                            str(self.a[6])+"\t"+str(self.a[7])+"\t"+str(self.a[8])))
    
    def paso2(self):
        self.m[2]=((self.m[4]*self.m[2])-(self.m[1]*self.m[5]))/self.m[0]
        self.m[8]=((self.m[4]*self.m[8])-(self.m[5]*self.m[7]))/self.m[0]
        self.a[0]=((self.m[4]*self.a[0])-(self.m[1]*self.a[3]))/self.m[0]
        self.a[1]=((self.m[4]*self.a[1])-(self.m[1]*self.a[4]))/self.m[0]
        self.a[2]=((self.m[4]*self.a[2])-(self.m[1]*self.a[5]))/self.m[0]
        self.a[6]=((self.m[4]*self.a[6])-(self.m[7]*self.a[3]))/self.m[0]
        self.a[7]=((self.m[4]*self.a[7])-(self.m[7]*self.a[4]))/self.m[0]
        self.a[8]=((self.m[4]*self.a[8])-(self.m[7]*self.a[5]))/self.m[0]
        self.m[0]=((self.m[4]*self.m[0])-(self.m[1]*self.m[3]))/self.m[0]
        self.m[7]=0
        self.m[1]=0
        self.piv3.configure(text="pivote ant. = "+str(self.m[4])+"\npivote act. = "+str(self.m[8]))
        self.matriz2.configure(text=(str(self.m[0])+"\t"+str(self.m[1])+"\t"+str(self.m[2])+"\n\n" +
                                str(self.m[3])+"\t"+str(self.m[4])+"\t"+str(self.m[5])+"\n\n" +
                                str(self.m[6])+"\t"+str(self.m[7])+"\t"+str(self.m[8])))
        self.adj2.configure(text=(str(self.a[0])+"\t"+str(self.a[1])+"\t"+str(self.a[2])+"\n\n" +
                            str(self.a[3])+"\t"+str(self.a[4])+"\t"+str(self.a[5])+"\n\n" +
                            str(self.a[6])+"\t"+str(self.a[7])+"\t"+str(self.a[8])))

    def paso3(self):
        self.a[0]=((self.m[8]*self.a[0])-(self.m[2]*self.a[6]))/self.m[4]
        self.a[1]=((self.m[8]*self.a[1])-(self.m[2]*self.a[7]))/self.m[4]
        self.a[2]=((self.m[8]*self.a[2])-(self.m[2]*self.a[8]))/self.m[4]
        self.a[3]=((self.m[8]*self.a[3])-(self.m[5]*self.a[6]))/self.m[4]
        self.a[4]=((self.m[8]*self.a[4])-(self.m[5]*self.a[7]))/self.m[4]
        self.a[5]=((self.m[8]*self.a[5])-(self.m[5]*self.a[8]))/self.m[4]
        self.m[0]=self.m[8]
        self.m[4]=self.m[8]
        self.m[7]=0
        self.m[1]=0
        self.m[2]=0
        self.m[5]=0
        self.matriz3.configure(text=(str(self.m[0])+"\t"+str(self.m[1])+"\t"+str(self.m[2])+"\n\n" +
                                str(self.m[3])+"\t"+str(self.m[4])+"\t"+str(self.m[5])+"\n\n" +
                                str(self.m[6])+"\t"+str(self.m[7])+"\t"+str(self.m[8])))
        self.adj3.configure(text=(str(self.a[0])+"\t"+str(self.a[1])+"\t"+str(self.a[2])+"\n\n" +
                            str(self.a[3])+"\t"+str(self.a[4])+"\t"+str(self.a[5])+"\n\n" +
                            str(self.a[6])+"\t"+str(self.a[7])+"\t"+str(self.a[8])))
        self.det.configure(text="Determinante = "+str(self.m[0]))
        self.solx1.configure(text="x1 = "+str(int((self.a[0]+self.a[1]+self.a[2])/self.m[0])))
        self.solx2.configure(text="x2 = "+str(int((self.a[3]+self.a[4]+self.a[5])/self.m[0])))
        self.solx3.configure(text="x3 = "+str(int((self.a[6]+self.a[7]+self.a[8])/self.m[0])))
        self.inv = 'true'
        print("paso3")
    
    
    def limpiarEntradas(self):
        self.inv = 'false'
        self.m = np.zeros((9), dtype=int)
        self.a = np.zeros((9), dtype=int)
        self.entry1.delete(0,'end')
        self.entry2.delete(0,'end')
        self.entry3.delete(0,'end')
        self.entry4.delete(0,'end')
        self.entry5.delete(0,'end')
        self.entry6.delete(0,'end')
        self.entry7.delete(0,'end')
        self.entry8.delete(0,'end')
        self.entry9.delete(0,'end')
        self.entry10.delete(0,'end')
        self.entry11.delete(0,'end')
        self.entry12.delete(0,'end')
        self.matriz.configure(text="0\t0\t0\n\n" +
                                    "0\t0\t0\n\n" +
                                    "0\t0\t0")
        self.matriz1.configure(text="0\t0\t0\n\n" +
                                    "0\t0\t0\n\n" +
                                    "0\t0\t0")
        self.matriz2.configure(text="0\t0\t0\n\n" +
                                    "0\t0\t0\n\n" +
                                    "0\t0\t0")
        self.matriz3.configure(text="0\t0\t0\n\n" +
                                    "0\t0\t0\n\n" +
                                    "0\t0\t0")
        self.adj.configure(text="0\t0\t0\n\n" +
                                 "0\t0\t0\n\n" +
                                 "0\t0\t0")
        self.adj1.configure(text="0\t0\t0\n\n" +
                                 "0\t0\t0\n\n" +
                                 "0\t0\t0")
        self.adj2.configure(text="0\t0\t0\n\n" +
                                 "0\t0\t0\n\n" +
                                 "0\t0\t0")
        self.adj3.configure(text="0\t0\t0\n\n" +
                                 "0\t0\t0\n\n" +
                                 "0\t0\t0")
        self.solx1.configure(text="x1 = ")
        self.solx2.configure(text="x2 = ")
        self.solx3.configure(text="x3 = ")
        self.det.configure(text="Determinante = ")
        self.piv1.configure(text="pivote ant. = 1\npivote act. =")
        self.piv2.configure(text="pivote ant. = \npivote act. =")
        self.piv3.configure(text="pivote ant. = \npivote act. =")


    def traerEntradas(self):
        self.inv = 'false'
        self.m = np.zeros((9), dtype=int)
        self.a = np.zeros((9), dtype=int)
        try:
            self.m[0]= self.entry1.get()
        except ValueError:
            self.m[0]=0
        try:
            self.m[1]= self.entry2.get()
        except ValueError:
            self.m[1]=0
        try:
            self.m[2]= self.entry3.get()
        except ValueError:
            self.m[2]=0
        try:
            self.a[0]= self.entry4.get()
        except ValueError:
            self.a[0]=0
        try:
            self.m[3]= self.entry5.get()
        except ValueError:
            self.m[3]=0
        try:
            self.m[4]= self.entry6.get()
        except ValueError:
            self.m[4]=0
        try:
            self.m[5]= self.entry7.get()
        except ValueError:
            self.m[5]=0
        try:
            self.a[4]= self.entry8.get()
        except ValueError:
            self.a[4]=0
        try:
            self.m[6]= self.entry9.get()
        except ValueError:
            self.m[6]=0
        try:
            self.m[7]= self.entry10.get()
        except ValueError:
            self.m[7]=0
        try:
            self.m[8]= self.entry11.get()
        except ValueError:
            self.m[8]=0
        try:
            self.a[8]= self.entry12.get()
        except ValueError:
            self.a[8]=0

        self.paso1()
        self.paso2()
        self.paso3()

    def traerInversa(self):
        if self.inv=='true':
            self.m_inv[0] = (self.a[0]*-1)/self.m[0]
            self.m_inv[1] = (self.a[1]*-1)/self.m[0]
            self.m_inv[2] = (self.a[2]*-1)/self.m[0]
            self.m_inv[3] = (self.a[3]*-1)/self.m[0]
            self.m_inv[4] = (self.a[4]*-1)/self.m[0]
            self.m_inv[5] = (self.a[5]*-1)/self.m[0]
            self.m_inv[6] = (self.a[6]*-1)/self.m[0]
            self.m_inv[7] = (self.a[7]*-1)/self.m[0]
            self.m_inv[8] = (self.a[8]*-1)/self.m[0]
            window = customtkinter.CTkToplevel(self)
            window.geometry("400x200")
            window.title("Inversa")
            window.iconbitmap("logo.ico")
            txt_inv = customtkinter.CTkLabel(window, text=("{:.2f}".format(self.m_inv[0])+"\t"+"{:.2f}".format(self.m_inv[1])+"\t"+"{:.2f}".format(self.m_inv[2])+"\n\n" +
                                                        "{:.2f}".format(self.m_inv[3])+"\t"+"{:.2f}".format(self.m_inv[4])+"\t"+"{:.2f}".format(self.m_inv[5])+"\n\n" +
                                                        "{:.2f}".format(self.m_inv[6])+"\t"+"{:.2f}".format(self.m_inv[7])+"\t"+"{:.2f}".format(self.m_inv[8])))
            txt_inv.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        else:
            print("no hay")

    

    def callback(self, P):
        if P.lstrip("+-").isdigit() or P == "":
        #if str.isdigit(P) or P == "":
            return True
        else:
            return False



if __name__ == "__main__":
    app = App()
    app.mainloop()