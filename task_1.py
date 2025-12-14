numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
N = [num for num in numbers if num is not None]
l = len(numbers)
S = sum(N)
Sr = S / l
# 5. Заменяем пропущенный элемент
numbers[4] = Sr
print("Измененный список:", numbers)