# Задача решается перебором

# Дано
"""
s = int(input())
(код программы)
print(n)
"""
# Алгоритм
"""
for i in range(1000):
    s = i
    (код программы)
    if n == (число из условия):
        print(i)
"""



# Определите, при каком наименьшем введённом значении переменной s программа выведет число 600. 
# Для Вашего удобства программа представлена на четырёх языках программирования. 

"""
s = int(input())
n = 300
while s + n < 400:
    s = s - 5
    n = n + 10
print(n)
"""
for i in range(1000):
    s=i
    n=300
    while s+n<400:
        s-=5
        n+=10
    if n==600:
        print(i)
