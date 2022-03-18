from matplotlib import pyplot as plt
import random
import math


fig, ax = plt.subplots()
ax.set_title('График')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')

n = int(input())
n += 1

print("Выберите способ оснащения:")
print("1 - левые точки")
print("2 - правые точки")
print("3 - точки посередине")
print("4 - случайные точки")
number = int(input())
sum = 0
i = 0
delta = math.pi/ n
x = [float(delta * i + delta/ 2) for i in range(n)]
y = []
if number == 1:
    for i in range(n): #левые точки
        sum += delta * math.cos(i * math.pi/ n)
        y.append(math.cos(x[i] - delta/2))
    plt.bar(x, y, width=delta, label = "Интегральная сумма")
if number == 2:
    for i in range(1, n + 1):#правые точки
        sum += delta * math.cos(i * math.pi/ n)
        y.append(math.cos(i* math.pi/n))
    plt.bar(x, y, width=delta, label="Интегральная сумма")
if number == 3:
    for i in range(n): # средние точки
        sum += delta * math.cos((i * math.pi / n + (i+1 )* math.pi / n)/2)
        y.append(math.cos((i * math.pi / n + (i+1 )* math.pi / n)/2))
    plt.bar(x, y, width=delta, label="Интегральная сумма")
if number == 4:
    for i in range(n):#  рандомные точки
        const = random.uniform(math.pi * i/n, math.pi * (i + 1)/n)
        sum += delta * math.cos(const)
        y.append(math.cos(const))
    plt.bar(x, y, width=delta, label="Интегральная сумма")




ax.hlines(0,0,3.14,color = 'black', alpha = 0.5)
print(sum)
ax.legend(loc='upper right')
plt.show()
