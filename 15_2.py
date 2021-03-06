""" Операция    | Аналог в Python   | Название 
        ∧       |       and         | Конъюнкция
        ∨       |       or          | Дизъюнкция
        ≡       |       ==          | Эквиваленция
        =       |       ==          | Равно
        ≠       |       !=          | Не равно
        →       |       <=          | Импликация
        ¬       |       not()       | Отрицание
Делимость-------------------------------------------------------
      Дел(n,m)  |      n%m == 0     | Делится без остатка
Коньюнкция------------------------------------------------------
        &       |       &           | Поразрядная конъюнкция
Множества-------------------------------------------------------
        ∈       |       in          | Принадлежит
Отрезки---------------------------------------------------------
P = [a;b] x ∈ P |  a <= x <= b      | x лежит на отрезке P
Длина отрезка - (b-a)
"""

"""
Как задаем множества:
1. Так же как и в условии 
    P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
2. Пустое множесво
    А = set()
3. Большое множество
    A = set(range(1,1000))
Операции с множествами
1. Добавить элемент
    А.add(x)
2. Убрать элемент
    A.remove(x)
"""
##############################################################################################################
"""
На Множества два принципиально разных случая:
1. Наименьшее количество элементов
    1) Изначально А пустое
    2) Кладем все x для которых f(x) ложно"""
# Элементами множеств А, P, Q являются натуральные числа, причём 
# P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}, 
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. 
# Известно, что выражение
#   ((x ∈ P) → (x ∈ A)) ∨ (¬(x ∈ A) → ¬(x ∈ Q))
# истинно (то есть принимает значение 1) при любом значении переменной х. 
# Определите наименьшее возможное количество элементов в множестве A.

P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
A = set()
def f(x):
    return((x in P) <= (x in A)) or ((not(x in A)) <= (not(x in Q)))

for x in range(1,1000):
    if f(x) == 0:
        A.add(x)
print(A)
"""
2. Наибольшее количество элементов
    1) Изначально А большое
    2) Убираем все x для которых f(x) ложно"""
# Элементами множеств А, P, Q являются натуральные числа, причём P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. Известно, что выражение
# ((x ∈ A) → (x ∈ P)) /\ ((x ∈ Q) → ¬ (x ∈ А))
# истинно (то есть принимает значение 1) при любом значении переменной х. 
# Определите наибольшее возможное количество элементов в множестве A.

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
A = set(range(1,1000))
def f(x):
    return((x in A) <= (x in P)) and ((x in Q) <= (not(x in A)))
flag = False
for x in range(1,1000):
    if f(x) == 0:
        A.remove(x)
print(A)
##############################################################################################################

# На числовой прямой даны два отрезка: P = [4; 15] и Q = [12; 20]. 
# Укажите наименьшую возможную длину такого отрезка A, что формула
#   ((x ∈ P) ⋀ (x ∈ Q)) → (x ∈ A)
# истинна при любом значении переменной х, т.е. принимает значение 1 при любом значении переменной х.

def f(x,a,b):
    return ((4 <= x <= 15) and (12<= x <= 20)) <= (a <= x <= b)

a = [] # массив для подходящих отрезков
for a in range(1,100): # перебираем левую(а) и правую(b) границу отрезка A = [a,b]
    for b in range(a,100):
        flag = True
        for x in range(1000): # Для всех x Функция должна быть истина
            if f(x,a,b)==0: # Если ложь
                flag = False # То эти а и b не подходя
                break
        if flag:
            a.append(b-a) # добавляем в массив длину отрезка [a,b]
print(min(a)) # находим минимальную длину




    