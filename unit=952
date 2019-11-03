# Заполняем первую матрицу
matrix = []
line = ''

while True:
    line = input()
    if line == 'end':
        break
    matrix.append([int(i) for i in line.split()])

# Проверяем размеры матрицы
length, width = 0, 0

for i in matrix:
    for j in i:
        width = len(i)
    length = len(matrix)
print('Длинна матрицы - {}, ширина - {}'.format(length, width))

# Создаем новую матрицу в которой будем заменять значения
new = [[0 for j in range(0, width)] for i in range(0, length)]

for i in range(0, len(new)):
    for j in range(0, width):
        x, y = i, j
        if x == 0:
            x = 1

        new[i][j] = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]

print(new)


