import matplotlib.pyplot as plt

Etiquetas=['Enero','Febrero','Marzo','Abril']
Valores=[4,5,3,2]
Colores=['green','orange','red','purple']

"""
Creando una grafica sencilla de barras, usamos el metodo bar
seguido de sus etiquetas y sus valores
"""

figura1=plt.figure(1)

plt.bar(Etiquetas,Valores)

#plt.show

"""
Podemos agregarle sus titulos
"""
figura2=plt.figure(2)
plt.bar(Etiquetas,Valores)

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')

#plt.show

"""
Podemos cambiar el color de las barras con el parametro color
"""
figura3=plt.figure(3)

plt.bar(Etiquetas,Valores,color='red')
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')
plt.show()















"""figura, ((ejemplo1, ejemplo2), (ejemplo3, ejemplo4))=plt.subplots(nrows=2,ncols=2)
plt.show()"""