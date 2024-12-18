class Polynomial:
    # Инициализация многочлена: [1, 2, 3] соответствует 3x^2 + 2x + 1.
    def __init__(self, coeff):
        # Делаем список
        self.coeff = list(coeff)
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

def create_polynomial():

        while True:
            try:
                coeffs_str = input("Введите коэффициенты многочлена через пробел (от младшего к старшему): ")
                coeffs = list(map(float, coeffs_str.split()))
                return Polynomial(coeffs)
            except ValueError:
                print("Ошибка: Введите числа, разделенные пробелами.")

def get_point():

        while True:
            try:
                x_str = input("Введите значение точки, в которой нужно вычислить многочлен: ")
                x = float(x_str)
                return x
            except ValueError:
                print("Ошибка: Введите число.")


if __name__ == "__main__":
        # Ввод многочленов с клавиатуры
        print("Ввод первого многочлена:")
        poly1 = create_polynomial()
        print("Ввод второго многочлена:")
        poly2 = create_polynomial()
        # Вывод
        print(f"Многочлен 1: {poly1}")
        print(f"Многочлен 2: {poly2}")
        print()

        # Складываем
        poly_sum = poly1 + poly2
        print(f"Сумма многочленов: {poly_sum}")
        print()

        # Точка
        x_val = get_point()

        # Вычисляем значение в точке
        print(f"Значение многочлена 1 в точке x = {x_val}: {poly1.evaluate(x_val)}")
        print(f"Значение многочлена 2 в точке x = {x_val}: {poly2.evaluate(x_val)}")

        # Вычисляем и выводим производную
        deriv_poly1 = poly1.derivative()
        deriv_poly2 = poly2.derivative()
        print(f"Производная многочлена 1: {deriv_poly1}")
        print(f"Производная многочлена 2: {deriv_poly2}")
        print()


