mtx1 = []
mtx2 = []
opr = input("Введите операцию (+ или * ): ")
print("Введите 1-ую матрицу")
for x in range(3):
    s = []
    for y in range(3):
        s.append(int(input()))
    mtx1.append(s)
for x in range(3):  # Вид 1-ой матрицы
    for y in range(3):
        print(mtx1[x][y], end=" ")
    print()
print("Введите 2-ую матрицу")
mtx2 = []
for x in range(3):
    s = []
    for y in range(3):
        s.append(int(input()))
    mtx2.append(s)
for x in range(3):  # Вид 2-ой матрицы
    for y in range(3):
        print(mtx2[x][y], end=" ")
    print()
print()

if opr == "+":
    for x in range(3):
        for y in range(3):
            mtx1[x][y] += mtx2[x][y]
elif opr == "*":
    for x in range(3):
        for y in range(3):
            mtx1[x][y] *= mtx2[x][y]
else:
    print("Ошибка. Команда не выполнена")
for x in range(3):
    for y in range(3):
        print(mtx1[x][y], end=" ")
    print()