num = input('Введите число: ')
sum = 0
for a in num:
    if a.isdigit():
        sum += int(a)

print(f"Сумма {num} равна: ", sum)