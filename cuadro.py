from colored import bg,attr

class Cuadro:
    def __init__(self, colores):
        self.cuadro = []
        self.colores = colores

    def colorsito(self, color):
        lista = {
            'rojo': bg('red'),
            'azul': bg('blue'),
            'verde': bg('green'),
            'amarillo': bg('yellow'),
            'verde_retro': bg('light_green'),
            'naranja_retro': bg('light_yellow'),
            'reset': attr('reset')
        }
        return lista.get(color, bg('white'))

    def actualizar_cuadro(self, turno, adivinanza, retroalimentacion):
        self.cuadro.append((adivinanza, retroalimentacion))

    def mostrar_cuadro(self):
        for turno, (adivinanza, retroalimentacion) in enumerate(self.cuadro):
            adivinanza_colores = ' '.join([self.colorsito(color) + '●' + self.colorsito('reset') for color in adivinanza])
            retroalimentacion_colores = ' '.join([self.colorsito('verde_retro') + '●' + self.colorsito('reset') if r == 'verde' else self.colorsito('naranja_retro') + '●' + self.colorsito('reset') for r in retroalimentacion])
            print(f"Turno {turno + 1}: {adivinanza_colores} | Retroalimentación: {retroalimentacion_colores}")
    



