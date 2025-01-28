import math

class DistanciaPuntos:
    def _init_(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def pedir_coordenadas(self):
        """Método para solicitar las coordenadas al usuario."""
        self.x1 = float(input("Ingrese la coordenada x1: "))
        self.y1 = float(input("Ingrese la coordenada y1: "))
        self.x2 = float(input("Ingrese la coordenada x2: "))
        self.y2 = float(input("Ingrese la coordenada y2: "))

    def calcular_distancia(self):
        """Método que calcula la distancia entre los dos puntos."""
        return math.sqrt((self.x2 - self.x1) * 2 + (self.y2 - self.y1) * 2)

    def mostrar_distancia(self):
        """Método para imprimir la distancia calculada."""
        print(f"La distancia entre ({self.x1}, {self.y1}) y ({self.x2}, {self.y2}) es: {self.calcular_distancia():.2f}")

def main():
    obj = DistanciaPuntos()  # Se crea el objeto sin valores iniciales
    obj.pedir_coordenadas()  # Se solicitan las coordenadas al usuario
    obj.mostrar_distancia()  # Se calcula y muestra la distancia

if __name__ == "__main__":
    main()