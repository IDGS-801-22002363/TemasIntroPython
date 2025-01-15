
# Imprimir las tablas de multiplicar del 1 al 10
for i in range(1, 11):  # Para cada número del 1 al 10
    print(f"Tabla del {i}:")
    for j in range(0, 11):  # Multiplicamos por 0 hasta 10
        print(f"{i} x {j} = {i * j}")
    print()  # Línea en blanco para separar las tablas