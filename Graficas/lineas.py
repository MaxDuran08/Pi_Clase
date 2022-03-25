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


#eje_x = ['Huawei','Apple','Xiaomi', 'LG','Motorola'] 
#eje_y = [10,20,30,15,5]

plt.plot(eje_x, eje_y)

plt.title(title)

plt.xlabel(xlabel)

plt.ylabel(ylabel)

#It will save the image on the root project and then will open the image

plt.savefig(f'lineamarzo.png')
file_name = f'lineamarzo.png'
img = Image.open(file_name)
img.show()