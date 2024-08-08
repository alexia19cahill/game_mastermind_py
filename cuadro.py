from colored import bg,attr

class Cuadro:
    def __init__(self, colores):
        self.cuadro = [['●','●','●','●'] for _ in range(12)]
        self.cuadro_ayuda = [['●','●','●','●'] for _ in range(12)]
        self.colores = colores

    def colorsito(self, color):
        lista = {
            'rojo': bg('red'),
            'azul': bg('blue'),
            'verde': bg('green'),
            'amarillo': bg('yellow'),
            'verde_retro': bg('light_green'),
            'naranja_retro': bg('light_yellow'),
            'negro': bg('black'),
            'reset': attr('reset')
        }
        return lista.get(color, bg('black'))

    def actualizar_cuadro(self, turno, adivinanza, retroalimentacion):
        self.cuadro[turno]=adivinanza
        self.cuadro_ayuda[turno]=retroalimentacion
        print(retroalimentacion)

    def mostrar_cuadro(self):
        for adivinanza, retroalimentacion in zip(self.cuadro, self.cuadro_ayuda):
            adivinanza_colores = ' '.join([self.colorsito(color) + ' ● ' + self.colorsito('reset') for color in adivinanza])
            retroalimentacion_colores = ' '.join([self.colorsito('verde_retro') + ' ● ' + self.colorsito('reset') if r == 'verde' else self.colorsito('naranja_retro') + ' ● ' + self.colorsito('reset') if r == "naranja" else self.colorsito('negro') + ' ● ' + self.colorsito('reset') for r in retroalimentacion])
            print(f"| {adivinanza_colores} |{retroalimentacion_colores}|")




