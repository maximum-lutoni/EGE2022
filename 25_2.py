# Пусть M – сумма минимального и максимального натуральных делителей целого числа, не считая 
# единицы и самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю.  
# Напишите программу, которая перебирает целые числа, большие 452021, в порядке возрастания и 
# ищет среди них такие, для которых значение M при делении на 7 дает в остатке 3. Вывести первые
# 5 найденных чисел и соответствующие им значения M. 

# Формат вывода: 
# для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число,
# затем значение M. Строки выводятся в порядке возрастания найденных чисел. 
# Например, для числа 20 M = 2 + 10 = 12. Количество строк в таблице для ответа избыточно.


# В данном прототипе мы не знаем сколько чисел перебрать, поэтому пользуемся while.
# Для того чтобы найти число M нам нужно найти делители числа => Ищем делители, считаем М, проверяем подходит ли M по условию.
k = 0      # счетчик подходящих чисел
i = 452022 # первое число, которе будем проверять
while k != 5: # пока не найдем 5 чисел
    a = []    # создаем массив делителей
    M = 0     # и М
    for j in range(2, i):
        if i % j == 0:
            a.append(j)
    # если делители найдены (в массиве делителей хотя бы 2 числа)
    if len(a) > 1:
        M = a[0] + a[-1]     # cчитаем М
        if M % 7 == 3:       # проверяем условие
            print(i, M)      # если число подходит сразу выводим его на экран
            k += 1           # не забываем посчитать что мы нашли число
    i += 1   # и не забываем изменить число, в отличии от for в while это нужно делать самостоятельно
