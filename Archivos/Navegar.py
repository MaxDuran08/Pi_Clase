import easygui

path_file = easygui.fileopenbox()
print(path_file)

file = open(path_file, 'r+')
texto = file.read()
file.close()

print(texto)
