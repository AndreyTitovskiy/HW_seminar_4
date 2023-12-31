# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов: "))
berries = []
for i in range(n):
    a = int(input(f"Введите количество ягод на кусте - {i+1}: "))
    berries.append(a)
max_collected = 0
for i in range(n):
    collected = berries[i] + berries[(i + 1) % n] + berries[(i - 1) % n]
    max_collected = max(max_collected, collected)

print("Максимальное число ягод:", max_collected)
