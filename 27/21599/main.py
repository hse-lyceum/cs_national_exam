# расстояние между точками
def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# для функции kx + b возвращает значение k и b по двум точкам
def linear_coeffs(p1, p2):
    if p1[0] != p2[0]:
        k = (p1[1] - p2[1]) / (p1[0] - p2[0])
    else:
        k = None
    if k is not None:
        b = p1[1] - k * p1[0]
    else:
        b = None
    return k, b

# вычисляет сумму расстояний в сегменте (список точек) от точки с заданным индексом до остальных точек
def sum_of_distances(segm, index_point):
    sum_of_dist = 0
    for i, point in enumerate(segm):
        if i != index_point:
            sum_of_dist += dist(point, segm[index_point])
    return sum_of_dist

# возвращает координаты центроида для заданного сегмента
def centroid(current_segment):
    min_index, min_dist = 0, sum_of_distances(current_segment, 0)
    for i in range(len(current_segment)):
        d = sum_of_distances(current_segment, i)
        if d < min_dist:
            min_dist, min_index = d, i
    return current_segment[min_index][0], current_segment[min_index][1]


print("*" * 15, "Part A", "*" * 15, "\n")

# Уравнения границы решения
lines = [([5, -5], [30, 15]), ([10, -10], [35, 5]) ]
for i in range(len(lines)):
    k, b = linear_coeffs(lines[i][0], lines[i][1])
    print(f"Разделитель {i+1}: k = {k}, b = {b}")



# Считываем точки из файла
with open('27_A_21599.txt') as F:
    for line in F:
        points = [[float(x), float(y)] for line in F for x, y in [line[:-1].replace(',', '.').split('\t')]]

# Сегментация
number_of_segments = 3
segments = [[] for _ in range(number_of_segments)]
for x, y in points:
    if y > 0.8 * x - 9.0:
        seg = 0
    elif y < 0.6 * x - 16.0:
        seg = 2
    else:
        seg = 1
    segments[seg].append([x, y])
print(f"Число сегментов: {number_of_segments}")
for i, segm in enumerate(segments):
    print(f"Сегмент {i + 1}: {len(segm)} точек")

# Поиск центроидов
centroids = [centroid(segment) for segment in segments]
print("Центроиды:")
for i, cent in enumerate(centroids):
    print(f"Центроид {i + 1}: x = {cent[0]}, y = {cent[1]}")

# Поиск средних
Px = sum(x for x, y in centroids) / len(centroids)
Py = sum(y for x, y in centroids) / len(centroids)

# Печать ответа
print(f"Ответ: {int(abs(Px * 10000))} {int(abs(Py * 10000))}\n\n")


print("*" * 15, "Part B", "*" * 15, "\n")

# Уравнения границ решения (разделителей)
lines = [([-10, -5], [-25, 25]),
         ([-10, 0], [-10, 25]),
         ([-10, -5], [10, 25]),
         ([-10, -5], [25, 15]),
         ([-30, -5], [25, -5])]
for i in range(len(lines)):
    k, b = linear_coeffs(lines[i][0], lines[i][1])
    print(f"Разделитель {i+1}: k = {k}, b = {b}")

# Считываем точки из файла
with open('27_B_21599.txt') as F:
    points = [[float(x), float(y)] for line in F for x, y in [line[:-1].replace(',', '.').split('\t')]]


# Сегментация
number_of_segments = 6
segments = [[] for _ in range(number_of_segments)]
for x, y in points:
    if y < -5.0:
        seg = 5
    elif y < x * (-2.0) -25.0:
        seg = 0
    elif x < -10:
        seg = 1
    elif y > x * 1.5 + 10.0:
        seg = 2
    elif 0.5714285714285714 * x + 0.7142857142857135 < y < x * 1.5 + 10.0:
        seg = 3
    else:
        seg = 4
    segments[seg].append([x, y])
print(f"Число сегментов: {number_of_segments}")
for i, segm in enumerate(segments):
    print(f"Сегмент {i + 1}: {len(segm)} точек")

# Поиск центроидов
centroids = [centroid(segment) for segment in segments]
print("Центроиды:")
for i, cent in enumerate(centroids):
    print(f"Центроид {i + 1}: x = {cent[0]}, y = {cent[1]}")

# Поиск средних
Px = sum(x for x, y in centroids) / len(centroids)
Py = sum(y for x, y in centroids) / len(centroids)

# Печать ответа
print(f"Ответ: {int(abs(Px * 10000))} {int(abs(Py * 10000))}\n\n")