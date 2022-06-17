#  Напишите программу, которая ищет среди целых чисел, принадлежащих 
#  числовому отрезку [851076; 851200], простые числа. Для каждого
#  найденного числа запишите порядковый номер числа в этом промежутке
#  и само число в порядке убывания.  

# Например, в диапазоне [20; 30] ровно два простых числа 23 и 29, поэтому
# для этого диапазона вывод на экране должен содержать следующие значения:
# 2 29
# 1 23

с = 0
for i in range(851076, 851201): # не забываем для второго числа брать +1
    k = 0
    # Проверка на простоту: 
    # перебираем все числа до заданного и проверяем делимость числа на выбранное.
    for j in range(2,i):
        if i % j == 0:
            k += 1 
            break
    # Если делителей не нашлось то число простое
    if k == 0:
            с += 1
            print(с, i)
