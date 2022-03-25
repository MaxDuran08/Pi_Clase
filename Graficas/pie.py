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


site_y = np.array(eje_y)
print(site_y)
labels_pie = eje_x
plt.pie(site_y, labels= labels_pie)

plt.title(f'{title}')

plt.xlabel(f'{xlabel}')


plt.ylabel(ylabel)
 
#It will save the image on the root project and then will open the image
plt.savefig(f'piemarzo.png')
file_name = f'piemarzo.png'
img = Image.open(file_name)
img.show()