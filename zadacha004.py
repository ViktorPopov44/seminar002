f = open("file.txt", "r")
a, b = f.read().split("\n")

# Перевод строк в числа, в указатели на индексы
a, b = int(a)-1, int(b)-1

N = int(input("Введите количество чисел: "))

# Формирование массива чисел от -N до N
A = []

for i in range(-N, N+1):
    A.append(i)

# Перемножение указанных позиций
res = A[a] * A[b]

# Вывод результатов
print(f"Position one: {a+1}\nPosition two: {b+1}\nNumber of elements: {N}\n{A}\n{res}")