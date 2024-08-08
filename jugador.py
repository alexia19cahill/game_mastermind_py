
class JugadorCrea:
    def __init__(self, colores):
        self.colores = colores

    def crear_codigo(self):
        while True:
            entrada = input(f"4 colores de {self.colores}, con  espacios: ").strip().lower()
            codigo = entrada.split()
            if len(codigo) == 4 and all(color in self.colores for color in codigo):
                return codigo
            else:
                print(f"ingresar 4 colores de {self.colores}.")

    

class JugadorAdivinado:
    def __init__(self, colores):
        self.colores = colores

    def adivinanza(self):
        while True:
            entrada = input(f"Adivina los 4 colores de {self.colores}, con espacios: ").strip().lower()
            adivinanza = entrada.split()
            if len(adivinanza) == 4 and all(color in self.colores for color in adivinanza):
                return adivinanza
            else:
                print(f" ingresar 4 colores de {self.colores}.")