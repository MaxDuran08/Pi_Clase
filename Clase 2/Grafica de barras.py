import matplotlib.pyplot as plt

Etiquetas=['Enero','Febrero','Marzo','Abril']
Valores=[4,5,3,2]

Archivo=open("./Clase 2/info.txt","r+")
info=Archivo.read()
print(info)
info=info.split("\n")
print(info)
Etiquetas=info[0].split(",")
Valores=[]
for x in info[1].split(","):
    Valores.append(int(x))
Color=str(info[2])
"""
Creando una grafica sencilla de barras, usamos el metodo bar
seguido de sus etiquetas y sus valores
"""

figura1=plt.figure(1)

plt.bar(Etiquetas,height=Valores)

#plt.show

"""
Podemos agregarle sus titulos
"""
figura2=plt.figure(2)
plt.bar(Etiquetas,height=Valores)

plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')

#plt.show

"""
Podemos cambiar el color de las barras con el parametro color
"""
figura3=plt.figure(3)

plt.bar(Etiquetas,height=Valores,color='red')
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')
#plt.show()


"""
Colores para cada uno
"""

figura4=plt.figure(4)

Colores=["red","green","blue","purple"]

plt.bar(Etiquetas,height=Valores,color=Colores)
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')
#plt.show()


"""
ancho de la grafica
"""
figura5=plt.figure(5)

plt.bar(Etiquetas,height=Valores,color=Colores,width=0.5)
plt.xlabel('Etiquetas')
plt.ylabel('Valores')
plt.title('Grafica de barras')
plt.show()












"""figura, ((ejemplo1, ejemplo2), (ejemplo3, ejemplo4))=plt.subplots(nrows=2,ncols=2)
plt.show()"""