class Polynomial:
    # Инициализация многочлена: [1, 2, 3] соответствует 3x^2 + 2x + 1.
    def init(self, cof):
        # Делаем список
        self.cof = list(cof)
        # Убираем ненужные нули в конце и список делаем
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        self.coeff = list(coeff)
        self._remove_leading_zeros()

    # Убираем нули в конце списка коэффициентов
    def _remove_leading_zeros(self):
        while len(self.coeff) > 1 and self.coeff[-1] == 0:
            self.coeff.pop()

    # Сложение 2 многочленов
    def __add__(self, second_poly):
        first_poly = self

        #Длина списка
        len_first = len(first_poly.coeff)
        len_second = len(second_poly.coeff)
        max_len = max(len_first, len_second)
        # Дополняем нулями если нужн
        padded_first = first_poly.coeff + [0] * (max_len - len_first)
        padded_second = second_poly.coeff + [0] * (max_len - len_second)
        # Складываем коэффициенты
        result_coeff = [padded_first[i] + padded_second[i] for i in range(max_len)]
        return Polynomial(result_coeff)



