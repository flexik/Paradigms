# Скрипт на Python для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами)
# с использованием функциональной парадигмы:

import numpy as np

def calculate_correlation(x, y):
    '''принимает два массива `x` и `y` и возвращает расчет корреляции Пирсона между ними'''
    n = len(x)
    # вычисляем среднее значение:
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # вычисляем ковариацию:
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    # NumPy для вычисления стандартного отклонения:
    std_dev_x = np.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    std_dev_y = np.sqrt(sum((yi - mean_y) ** 2 for yi in y))

    correlation = covariance / (std_dev_x * std_dev_y)
    return correlation

# Пример использования
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

correlation = calculate_correlation(x, y)
print("Correlation:", correlation)

# Значение коэффициента +1 означает наличие полной положительной линейной связи,
# а значение -1 наличие полной отрицательной линейной связи.