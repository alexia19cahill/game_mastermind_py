import random
from jugador import JugadorAdivinado, JugadorCrea
from cuadro import Cuadro

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
        elif cadivinanza[i] and cadivinanza[i] in scodigo:
            retroalimentacion.append('naranja')
            scodigo[scodigo.index(cadivinanza[i])] = None
        else:
            retroalimentacion.append("black")

    return retroalimentacion


def main():
    rol = input("¿Quieres ser el creador del codigo o el que adivina? (crear/adivinar): ").strip().lower()
    if rol == 'crear':
        jugador_creador = JugadorCrea(colores)
        codigo = jugador_creador.crear_codigo()
        
        print("********")
        cuadro = Cuadro(colores)
        jugador_adivinador = JugadorAdivinado(colores)
        for turno in range(12):
            adivinanza = codigo_aleatorio()
            retroalimentacion_result = retroalimentacion(adivinanza, codigo)
            cuadro.actualizar_cuadro(turno, adivinanza, retroalimentacion_result)
            cuadro.mostrar_cuadro()
            if retroalimentacion_result == ['verde', 'verde', 'verde', 'verde']:
                print("Felicidades adivinade el codigo.")
                break
            else:
                print(f"Perdiste 😂. El código era: {' '.join(codigo)}")
    elif rol == "adivinar":

        codigo = codigo_aleatorio()

        print("********")
        cuadro = Cuadro(colores)
        jugador_adivinador = JugadorAdivinado(colores)
        for turno in range(12):
            adivinanza = jugador_adivinador.adivinanza()
            retroalimentacion_result = retroalimentacion(adivinanza, codigo)
            cuadro.actualizar_cuadro(turno, adivinanza, retroalimentacion_result)
            cuadro.mostrar_cuadro()
            if retroalimentacion_result == ['verde', 'verde', 'verde', 'verde']:
                print("Felicidades adivinade el codigo.")
                break
        else:
            print(f"Perdiste 😂. El código era: {' '.join(codigo)}")
    else:
        print("adios")

if __name__ == "__main__":
    main()


