# Решение перебором по анологии с 6 заданием

# Ниже на четырёх языках программирования записан алгоритм. Получив на вход число x, 
# этот алгоритм печатает два числа: L и M. Укажите наименьшее число x, при вводе
# которого алгоритм печатает сначала 6, а потом 3.

"""
x = int(input())
L = 0
M = 0
while x > 0:
  M = M + 1
  if x % 2 != 0:
    L = L + x % 6
  x = x // 6
print(L)
print(M)
"""
for i in range(1000): # перебераем значения на вход
    x = i
    L = M = 0
    while x >0:
        M = M + 1
        if x%2 != 0:
            L = L + x%6
        x = x//8
    if L==6 and M == 3: # Если на выводе первое число 6, а второе 3 
      print(i) # то это значение подходит

