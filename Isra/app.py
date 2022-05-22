from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
import easygui
from RedNeuronal import RedNeuronal
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import threading
import matplotlib.animation as animation
import numpy as np

class app:
    def __init__(self,master):
        self.master = master
        self.master.title("Proyecto Isra")
        self.master.resizable(True,True)
        self.master.config(bg="green")
        self.imagen=None
        #self.master.iconbitmap(".\Imagenes\ico.ico")
        self.Gadgetts()

    def Gadgetts(self):
        self.miFrame=Frame()
        self.miFrame.pack()
        self.miFrame.config(bg="pale green")
        self.miFrame.config(width="900", height="700")


        botonCargarImagen = Button(self.miFrame,text="Cargar Imagen",bg="spring green",activebackground="lawn green",font=("Arial",12),command=self.CargarImagen)
        botonCargarImagen.place(x=20,y=40)

        botonAnalizar = Button(self.miFrame,text="Analizar",bg="spring green",activebackground="lawn green",font=("Arial",12),command=self.Analizar)
        botonAnalizar.place(x=175,y=40)


#Creas un frame encima del frame base
        self.FrameD=Frame(self.miFrame)
        self.FrameD.pack(fill=BOTH, expand=1)
        self.FrameD.place(x=20,y=80)
#le creas un lienzo=Canvas que estara en el nuevo frame, ahi es donde vamos a pintar      
        self.myCanvas=Canvas(self.FrameD)
        self.myCanvas.configure(width=700,height=540)
        self.myCanvas.pack(side=LEFT,fill=BOTH,expand=1)


        """fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(self.Data)

        canvas = FigureCanvasTkAgg(fig, master=self.myCanvas)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)"""

        """toolbar = NavigationToolbar2Tk(canvas, self.myCanvas)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)"""


    def CargarImagen(self):
        print("CArgar Archivo")
        self.imagen=easygui.fileopenbox(title="Seleccione una imagen.")
        

    def Analizar(self):
        print("Analizando")
        """if self.imagen!=None:
            print(f"La ruta es {self.imagen}")"""
        Red=RedNeuronal()
        Red.Aprender()
        Historial=Red.RetornarHistorial()
        #print(Historial.history["loss"])

        #Agregamos la grafica
        self.DataX=Historial.history["loss"]
        self.DataY=[]
        for y in range(len(Historial.history["loss"])):
            self.DataY.append(y)
        #print(self.DataY)
        self.fig, self.ax = plt.subplots()
        plt.title("Grafica en Tkinter con Matplotlib",color='black',size=16, family="Arial")

        self.ax.tick_params(direction='out', length=6, width=2,colors='black', grid_color='r', grid_alpha=0.5)

        self.line, =self.ax.plot(self.DataY,self.DataX)
        plt.xlim([-2,1002])
        plt.ylim([min(Historial.history["loss"]),max(Historial.history["loss"])]) 
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.myCanvas)  # A tk.DrawingArea.
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        animacion=animation.FuncAnimation(self.fig,self.Animar,interval=50, blit=True)
        self.canvas.draw()

        
    def Animar(self,parametro):
        self.line.set_ydata(self.DataX[parametro])
        return self.line,
    





root = Tk()
Ventana=app(root)
root.mainloop()