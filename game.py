import random


colores = ['rojo', 'azul', 'verde', 'amarillo']

def codigo_aleatorio():
    return [random.choice(colores) for _ in range(4)]


