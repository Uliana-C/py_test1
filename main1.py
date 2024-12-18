class Polynomial:
    # Инициализация многочлена: [1, 2, 3] соответствует 3x^2 + 2x + 1.
    def init(self, cof):
        # Делаем список
        self.cof = list(cof)
        # Убираем ненужные нули в конце
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        while len(self.cof) > 1 and self.cof[-1] == 0:
         
