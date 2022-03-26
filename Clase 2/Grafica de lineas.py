import matplotlib.pyplot as plt

"""
Para crear una grafica de lineas utilizamos el metodo plot y enviamos como parametro sus etiquetas primero
y luego sus valores de dichas etiquetas
"""

Etiquetas=['Enero','Febrero','Marzo','Abril']
Valores=[4,5,3,2]

ejemplo1 = plt.figure(1)

plt.plot(Etiquetas,Valores)
#plt.show()

"""
Agregamos titulos, su titulo general con .title, su titulo en x con x.label
y su titulo en y con .ylabel
"""
ejemplo2 = plt.figure(2)

plt.plot(Etiquetas,Valores)

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()



"""
Podemos modificar su apariencia:
para agregar marcadores (puntos) usamos el parametro marker y le enviamos un caracter valido
"""
ejemplo3 = plt.figure(3)

plt.plot(Etiquetas,Valores,marker="v")

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
Podemos agrandar el punto con el parametro markersize enviandole un entero
"""

ejemplo4 = plt.figure(4)

plt.plot(Etiquetas,Valores,marker="v",markersize=15)

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
Podemos cambiar el estilo de linea con el parametro linestyle y le enviamos su string 
"""

ejemplo5 = plt.figure(5)

plt.plot(Etiquetas,Valores,marker="v",markersize=15,linestyle=(0,(1,10)))

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
Podemos cambiar el color de la linea con el parametro color
"""

ejemplo6 = plt.figure(6)

plt.plot(Etiquetas,Valores,marker="v",markersize=15,linestyle=(0,(1,10)),color="gold")

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
Podemos agregar otra linea para comparar en nuestro lienzo haciendo otro plot
"""

ejemplo7 = plt.figure(7)

plt.plot(Etiquetas,Valores,marker="v",markersize=15,linestyle=(0,(1,10)),color="gold")

Valores2=[3,3,1,5]
plt.plot(Etiquetas,Valores2,marker="*",markersize=20,linestyle="--",color="cyan")

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
Podemos agregar una leyenda a nuestra grafica, primero agregamos labels a cada plot y luego usamos el metrodo legend
"""

ejemplo8 = plt.figure(8)

plt.plot(Etiquetas,Valores,marker="v",markersize=15,linestyle=(0,(1,10)),color="gold", label="2021")

plt.plot(Etiquetas,Valores2,marker="*",markersize=20,linestyle="--",color="cyan", label="2022")

plt.legend()

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')

#plt.show()

"""
podemos modificar la posicion de nuestra legenda dandole un parametro al metodo legend
y a legen le enviamos el parametro loc igualado a la posicion que precisemos
"""

ejemplo9 = plt.figure(9)

plt.plot(Etiquetas,Valores,marker="v",markersize=15,linestyle=(0,(1,10)),color="purple", label="2021")
plt.plot(Etiquetas,Valores2,marker="*",markersize=20,linestyle="--",color="cyan", label="2022")

plt.legend(loc=3)

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de lineas')


plt.show()

