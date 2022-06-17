# Массив — это набор данных одного типа (элементов массива), расположенных в 
# памяти компьютера непосредственно друг за другом и пронумерованных индексами. 

"""      НУМЕРАЦИЯ В МАССИВАХ С 0 
    Первый индекс 0, последний len(a)-1"""

# Инициализация массивов
a = [1, 2 , 3, 4] # Задаем сразу
a = []            # Создаем пустой массив
a.append()        # Добавить элемент в конец массива
a = [0]*n         # Создать массив из n нулей

# считывание/заполнение массива
a = []         #создали пустой массив 
n = int(input())
for i in range(n):         #в цикле с range=длина массива
    a.append(int(input())) #последовательно заносим в массив число или
    a.append(int(input())) #последовательно заносим в массив строку

# C файлом:
file = open("name.txt")
a = []         #создали пустой массив
n = int(file.readline())
for i in range(n):         #в цикле с range=длина массива
    a.append(int(file.readline())) #последовательно заносим в массив число или
    a.append(int(file.readline())) #последовательно заносим в массив строку

# Двойной for               # Перебирает все пары элементов (i,j) = (1,1)(1,2)(1,3)(1,4)...(1,n-1)
for i in range(n):          #                                       (2,1)(2,2)(2,3)(2,4)...(2,n-1)
    for j in range(n):      #                                       (3,1)(3,2)(3,3)(3,4)...(3,n-1)
        a[i],a[j]           #                                       (4,1)(4,2)(4,3)(4,4)...(4,n-1)
                            #                                       ..............................
                            #                                       (n-1,1)(n-1,2)(n-1,3)(n-1,4)...(n-1,n-1)
                            
