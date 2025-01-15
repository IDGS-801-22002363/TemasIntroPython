# Pedir al usuario que ingrese un número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Inicializar x
x = 0

# Usar un bucle while para imprimir la tabla de multiplicar
while x <= 10:
    print(f"{numero} x {x} = {numero * x}")
    x += 1  # Incrementar x en 1