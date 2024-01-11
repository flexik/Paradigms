# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Императивный стиль
def bubble_sort_desc(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers = [5, 2, 9, 1, 3]
bubble_sort_desc(numbers)
print(numbers)  # Вывод: [9, 5, 3, 2, 1]


# Декларативный стиль
numbers = [5, 2, 9, 1, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Вывод: [9, 5, 3, 2, 1]