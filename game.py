import random
from jugador import JugadorAdivina, JugadorCrea


colores = ['rojo', 'azul', 'verde', 'amarillo']

def codigo_aleatorio():
    return [random.choice(colores) for _ in range(4)]


def retroalimentacion(adivinanza, codigo):
    retroalimentacion = []
    scodigo = codigo[:]
    cadivinanza = adivinanza[:]

    for i in range(4):
        if adivinanza[i] == scodigo[i]:
            retroalimentacion.append('verde')
            cadivinanza[i] = scodigo[i] = None

    for i in range(4):
        if cadivinanza[i] and cadivinanza[i] in scodigo:
            retroalimentacion.append('naranja')
            scodigo[scodigo.index(cadivinanza[i])] = None

    return retroalimentacion


