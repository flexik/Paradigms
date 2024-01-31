# Программа на языке Python для бинарного поиска:

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
print(result)  # Вывод: 2