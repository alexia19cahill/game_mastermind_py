# game_mastermind_py
# game_mastermind_py

se utilizo coroled,ramdom,
hice una lista de colores disponibles (rojo, azul, verde, amarillo).
Se  instangcian las clases JugadorCrea y JugadorAdivinado.
se puede elige si quiere ser el creador del código o el adivinador.
 ingresa un código de 4 colores.
Se daretroalimentación y se actualiza el tablero después de cada intento.
El juego termina cuando el usuario acierta el código o se agotan los intentos.
Retroalimentación:
verde: Color correcto en la posición correcta.
naranja: Color correcto en la posición incorrecta.
negro: Color incorrecto.


JugadorCrea
__init__(self, colores): Inicializa la lista de colores disponibles.
crear_codigo(self): Permite al usuario crear un código de 4 colores.

JugadorAdivinado
__init__(self, colores): Inicializa la lista de colores disponibles.
adivinanza(self): Permite al usuario adivinar el código de 4 colores.
Cuadro

__init__(self, colores): Inicializa el tablero de juego.
colorsito(self, color): Devuelve el color de fondo correspondiente.
actualizar_cuadro(self, turno, adivinanza, retroalimentacion): Actualiza el tablero con la adivinanza y la retroalimentación.
mostrar_cuadro(self): Muestra el estado actual del tablero.
Funciones Generales

codigo_aleatorio(): Genera un código aleatorio de 4 colores.
retroalimentacion(adivinanza, codigo): Compara la adivinanza del jugador con el código y genera una retroalimentación.