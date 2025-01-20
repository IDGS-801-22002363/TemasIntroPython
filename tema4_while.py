x=0
while x<10:
    print(x)
    x=x+1

    '''operacion de multiplicacion de a x b utilizando sumas
    a=3
    b=4
    salida: 3+3+3+3=12
    '''
a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))

resultado = 0

for _ in range(b):
    resultado += a

print(f"La multiplicación {a} x {b} ( {a} sumado {b} veces) es igual a: {resultado}")

