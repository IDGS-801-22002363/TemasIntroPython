from io import open
import math

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readlines()
print(type(lectura))
#lectura= texto.read()
print(lectura)
for i in lectura:
    print(i)
#texto.write("Hola, soy un archivo de texto/n")
#texto.write("Hola, mundo/n")
texto.close()