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

        """
        No es lo mas optimo pero si hago el frame antes donde estan los gadgets se van haciendo graficas abajo de cada una, entonces cada vez que se analiza se crea este lienzo
        , esta mal va vos, por que se crea uno encima de otro cada vez que analizas
        """
        #Creas un frame encima del frame base
        self.FrameD=Frame(self.miFrame)
        self.FrameD.pack(fill=BOTH, expand=1)
        self.FrameD.place(x=20,y=80)
        #le creas un lienzo=Canvas que estara en el nuevo frame, ahi es donde vamos a pintar      
        self.myCanvas=Canvas(self.FrameD)
        self.myCanvas.configure(width=700,height=540)
        self.myCanvas.pack(side=LEFT,fill=BOTH,expand=1)

        print("Analizando")
        """if self.imagen!=None:

            print(f"La ruta es {self.imagen}")"""
        """Este tryo hace que se detenga el hilo de la animacion, digamo que cuando haces el metodo analizar y esta en proceso de animar, corta la animacion actual para
            empezar a hacer otra animacion"""
        try:
            self.animacion.event_source.stop()
        except:
            pass

        Red=RedNeuronal()
        Red.Aprender()
        Historial=Red.RetornarHistorial()

        #print(Historial.history["loss"])


        #Se crea los arreglos de los valores en X y Y
        self.DataX=Historial.history["loss"]

        self.DataY=[]
        for y in range(len(Historial.history["loss"])):
            self.DataY.append(y)

        #Se empieza a hacer la grafica
        self.fig, self.ax = plt.subplots()
        plt.title("Grafica en Tkinter con Matplotlib",color='black',size=16, family="Arial")

        self.ax.tick_params(direction='out', length=6, width=2,colors='black', grid_color='r', grid_alpha=0.5)

        #aqui le paso un arreglo vacio al crear la grafica pues despues va a actualizar los datos
        r=[]
        self.line, =self.ax.plot(r,r, color='r', marker='o',linewidth=3, markersize=1, markeredgecolor='m')

        #aqui se ponen los limites que tendra la grafica, digamos que en y le puse que sea max y min de los datos del arreglo de lo que aprendio
        #pero en x el 1002 digamos es el numero que vos le das de intentos para que aprenda y el -50 es para que este separado el eje en x=0 y no salga pegado a la pared
        plt.xlim([-50,1002])
        plt.ylim([min(Historial.history["loss"]),max(Historial.history["loss"])]) 
        
        #Aqui agrego la grafica al canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.myCanvas)  # A tk.DrawingArea.
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        #aqui se hace la animacion, en interval=5 el 5 es la velocidad que le puse para que grafique, si queres le podes pedir al usuario esa velocidad
        self.animacion=animation.FuncAnimation(self.fig,self.Animar,interval=5, blit=True, save_count=10)
        self.canvas.draw()
        

        #Esta funcion anima la grafica
    def Animar(self,parametro):
        self.line.set_data(self.DataY[:parametro],self.DataX[:parametro])
        return self.line,
    





root = Tk()
Ventana=app(root)
root.mainloop()