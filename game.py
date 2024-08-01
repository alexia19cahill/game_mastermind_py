colores = ['green', 'blue', 'red', 'yellow']
class cuadro:
    def _init_(self):
        self.cuadro = [['⚪', '⚪', '⚪', '⚪', '⚪'] for _ in range(12)]

    def mostrarcuadro(self):
        for linea in self.cuadro:
            print(' '.join(linea[:4]) + ' | ' + linea[4])