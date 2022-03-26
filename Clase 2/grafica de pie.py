import matplotlib.pyplot as plt

"""
Para las graficas de pie se usa plt.pie(), dandole como parametro sus valores numericos primero, luego las etiquetas de dichos valores
"""

Etiquetas=["Rojo","Morado","Oro","Indigo"]
Valores=[6,3,3,6]

ejemplo1=plt.figure(1)

plt.pie(Valores,labels=Etiquetas)
#plt.show()

"""
Le podemos agregar un titulo a la grafica con plt.title()
"""
ejemplo2=plt.figure(2)

plt.pie(Valores,labels=Etiquetas)
plt.title('Grafica de pie')
#plt.show()

"""
Podemos ir modificar visualmente nuestra grafica:
Cambiandole el color a la grafica:
enviando un arreglo con el nombre de los colores al parametro de colors
"""
ejemplo3=plt.figure(3)

Colores=["red","purple","gold","indigo"]

plt.pie(Valores,labels=Etiquetas,colors=Colores)
plt.title('Grafica de pie')
#plt.show()


"""
Agregar un desfase a nuestra grafica con el parametro explode, le enviamos un arreglo con las dimensiones del desfase
"""

ejemplo4=plt.figure(4)

Desfase=[0,0,0,0.1]

plt.pie(Valores,labels=Etiquetas,colors=Colores,explode=Desfase)
plt.title('Grafica de pie')
#plt.show()


"""
Cambiamos el color del texto con el parametro textprops
"""

ejemplo5=plt.figure(5)

plt.pie(Valores,labels=Etiquetas,colors=Colores,explode=Desfase,textprops=dict(color="cyan"))
plt.title('Grafica de pie')
#plt.show()


"""
Agregamos porcentajes a nuestra grafica con el parametro autopct
"""

ejemplo6=plt.figure(6)

plt.pie(Valores,labels=Etiquetas,colors=Colores,explode=Desfase,textprops=dict(color="cyan"),autopct="%i%%")
plt.title('Grafica de pie')
#plt.show()

"""
Con decimales
"""

ejemplo7=plt.figure(7)

plt.pie(Valores,labels=Etiquetas,colors=Colores,explode=Desfase,textprops=dict(color="cyan"),autopct="%0.1f%%")
plt.title('Grafica de pie')
#plt.show()

plt.show()


