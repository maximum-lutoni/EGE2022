# Необходимо найти в заданной серии показаний прибора минимальное чётное произведение двух показаний, 
# между моментами передачи которых прошло не менее 6 минут. Если получить такое произведение не удаётся, 
# ответ считается равным -1. Количество энергии, получаемое прибором за минуту, не превышает 1000 условных единиц.
# Общее количество показаний прибора в серии не превышает 100 000.

# Программа должна вывести одно число – описанное в условии произведение, либо -1, 
# если получить такое произведение не удаётся.

""" 
    Задача является усложнением задач 27_2. Добавилось растояние между элементами массива.
    Для ее решения будем использовать буферный массив. Буферный массив - массив для сохранения расстояния между элементами.
    Его длина = минимальному растоянию между элементами. Всегда обрабатываем первое число массива a[0] и введенное число x.
    От a[0] мы получаем информацию об уходящих числах (минимум, максимум, и т.д.), от х – о входящих.
"""

f = open('27.txt')   
n = int(f.readline()) 
# создаем и заполняем буферный массив длины 6
a = [int(f.readline()) for i in range(6)]
minx = 1001            # минимум 
min2 = 1001            # минимум кратный 2
minp = 1001 * 1001 + 1 # минимальное кратное произведение
for i in range(6, n):  # Первые 6 элементов уже считали поэтому начинаем с 6
    # берем первый элемент из нашего буферного массива и проводим его анализ на кратность и минимальность
    minx = min(a[0],minx) 
    if a[0] % 2 == 0:
        min2 = min(a[0],min2)
    x = int(f.readline()) # считываем новое значение (оно на расстояние 6 от нашего a[0])
    # обрабатываем x так же как и с обычным произведением 27_2
    p = min2 * x 
    if x % 2 == 0:
        p = min(minx * x,p)
    if p % 2 == 0:
        minp = min(p,minp)
    
    for j in range(5):
        a[j] = a[j + 1] # сдвигаем элементы буферного массива
    a[5] = x # добавляем в буфферный массив  текущий элемент
   
if minp != 1000 * 1000 + 1: # если нашли minp
    print(minp) # выводим
else: # если нет
    print(-1) # выводим -1

##############################################################################################################################

# По каналу связи передавалась последовательность положительных целых чисел, все числа не превышают 1000. 
# Количество чисел известно. Требуется найти количество чисел R, удовлетворяющих следующим условиям:
#   1) R — произведение двух различных переданных элементов последовательности, индексы которых различаются 
#   не менее чем на 3. («различные» означает, что не рассматриваются квадраты переданных чисел, произведения 
#   различных элементов последовательности, равных по величине, допускаются);
#   2) R делится на 21.

# Программа должна напечатать одно число — вычисленное количество возможных значений R, соответствующих условиям задачи.

"""" Аналог 27_3 Но с дополнением на расстояние. Так же дополняем буферным массивом. Остальное решение так же. """

f = open('27.txt') 
n = int(f.readline()) 
a = [int(f.readline()) for i in range(3)]   # буферный масив
c3 = 0         # количество кратных 3
c7 = 0         # количество кратных 7
c21 = 0        # количество кратных 21
c = 0          # количество R
for i in range(3, n):
    # обрабатываем первый элемент буферного массива на кратность
    if a[0] % 21 == 0:
        c21 += 1
    if a[0] % 7 == 0:
        c7 += 1
    if a[0] % 3 == 0:
        c3 += 1
    x = int(f.readline()) # cчитываем новый элемент
    # в зависимости от него считаем количество произведений
    if x % 21 == 0: # если он кратен 21
        c += i - 2  # умножаем на все элементы до
    elif x % 7 == 0: # если он кратен 7
        c += c3 # умножаем на элементы кратные 3
    elif x % 3 == 0: # если он кратен 3
        c += c7 # умножаем на элементы кратные 7
    else: # если число некратное
        c += c21 # умножаем на элементы кратные 21
    for j in range(2):
        a[j] = a[j + 1]  # cдвигаем буферный массив
    a[2] = x
print(c)

