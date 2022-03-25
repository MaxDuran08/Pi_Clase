import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

#,''
Etiquetas=['uno','dos','tres','cuatro']
Valores=['1','2','3','4']

"""Cambio de tamaño antes de crear la grafica, el tamaño sera general para todas las graficas,
solo aplica a el tamaño del primer figure.figsize
plt.rcParams["figure.figsize"] = (Largo, Altura)"""

figura1=plt.figure(1)
"""marker=> es para los puntos de interseccion
color=> es para el color de linea y scatter que contenga la figura
linestyle=> es para el estilo de la linea donde solo acepta:
'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
"""

plt.plot(Etiquetas,Valores,marker="p",linestyle="--",color="red", label="rojo")
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

"""Agregamos otra grafica en la misma figura"""

Valores=['5','4','2','3']

plt.plot(Etiquetas,Valores,'--g', marker="*", markersize=15, label="verde")
plt.show()


figura2=plt.figure(2)
plt.pie(Valores,labels=Etiquetas)
plt.title('Grafica de pie')

figura3=plt.figure(3)
plt.bar(Etiquetas,Valores)
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')

"""Cambio de tamaño despues de crear la grafica, usando la grafica 1
NombreVarriable=plt.figure(NumeroDeFigura)
NombreVariable.set_size_inches(Largo, Altura)"""

#figura1.set_size_inches(10,5)
#figura2.set_size_inches(5,5)
#figura3.set_size_inches(10,5)



#plt.show()


