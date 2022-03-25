import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import easygui


path_file = easygui.fileopenbox()

read_file = open(path_file, 'r+')
text = read_file.read()
read_file.close()


all_data = text.split('\n')

title = all_data[0]
xlabel = all_data[1]
ylabel = all_data[2]

eje_x = all_data[3].split(',')
eje_y = all_data[4].split(',')

#Barras
#eje_x = ['Huawei','Apple','Xiaomi', 'LG','Motorola'] 
#eje_y = [10,20,30,15,5] 

#Usarlo solo para graficar
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y)

#Titulo
ax.set_title(f'{title}')

#Nombre adicional
ax.set_xlabel(xlabel)

#Nombre adicional
ax.set_ylabel(ylabel)

#Guardar la imagen
plt.savefig(f'MARZO_2020.png')

#Para abrir la imagen
file_name = f'MARZO_2020.png'
img = Image.open(file_name)
img.show()