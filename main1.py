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

    # Вычисление значения многочлена в точке x
    def evaluate(self, x):
        result = 0  # Начинаем с 0
        # Идем по коэффициентам и степеням
        for power, coeff in enumerate(self.coeff):
            result += coeff * x ** power  # Вычисляем значение
        return result

    #Представим многочлен в виде строки
    def __str__(self):
        if not self.coeff:
            return "0"

        terms = []  # пустой список
        # Перебираем коэффициенты и степени
        for power, coeff in enumerate(self.coeff):
            if coeff == 0:
                continue  # Пропускаем нулевые коэффициенты

            if power == 0:
                term = f"{coeff}"  # свободный член
            elif power == 1:
                term = f"{coeff}x"  # член с x
            else:
                term = f"{coeff}x^{power}"  # член со степенью больше 1
            terms.append(term)  # добавляем строку в список

        # Соединяем строки в одну
        return " + ".join(reversed(terms)).replace(" + -", " - ").replace("+ -", "- ")

    #Найдем производную
    def derivative(self):
        # если многочлен константа - производная  0
        if len(self.coeff) <= 1:
            return Polynomial([0])

        derivative_coeffs = []
        for power, coeff in enumerate(self.coeff):
            if power > 0:
                derivative_coeffs.append(coeff * power)

        return Polynomial(derivative_coeffs)


