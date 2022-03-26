import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (8, 8)

figura, (ejemplo1,ejemplo2)= plt.subplots(nrows=2)
#Primera grafica=>
Colores=["gold","springgreen","violet","tan"]

ValoresM=[20,25,30,40,50]
ValoresH=[10,25,15,43,48]
Etiquetas=["G1","G2","G3","G4","G5"]

Posicion = np.arange(len(Etiquetas))  
ancho = 0.35  

r1=ejemplo1.bar(Posicion-ancho/2,ValoresM,ancho, label="Mujeres")
r2=ejemplo1.bar(Posicion+ancho/2,ValoresH,ancho, label="Hombres")

ejemplo1.set_ylabel("Valores")
ejemplo1.set_title("Titulo")
ejemplo1.set_xticks(Posicion, Etiquetas)
ejemplo1.legend()
ejemplo1.bar_label(r1, padding=1)
ejemplo1.bar_label(r2, padding=1)

#Segunda grafica=>

ejemplo2.plot(Etiquetas,ValoresM,marker="p",markersize=13,linestyle="dotted",color="purple", label="Hombres")
ejemplo2.plot(Etiquetas,ValoresH,marker="*",markersize=10,linestyle="--",color="cyan", label="Mujeres")

ejemplo2.legend()

ejemplo2.set_xlabel('Etiquetas')
ejemplo2.set_ylabel('Valores')
ejemplo2.set_title('Grafica de lineas')


figura.tight_layout()
plt.show()