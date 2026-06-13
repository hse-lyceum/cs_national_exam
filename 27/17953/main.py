def dist(star_1, star_2):
    return ((star_1[0] - star_2[0]) ** 2 + (star_1[1] - star_2[1]) ** 2) ** 0.5


def gravitational_interaction(star_1, star_2):
    return dist(star_1, star_2) * abs(star_1[2] - star_2[2])


def kx_plus_b(p1, p2):
    if p1[0] - p2[0] != 0:
        k = (p1[1] - p2[1]) / (p1[0] - p2[0])
    else:
        k = None
    if k is not None:
        b = p1[1] - k * p1[0]
    else:
        b = None
    return k, b


def total_gravitational_interaction(cluster, star_index):
    s = 0
    for i in range(len(cluster)):
        if i != star_index:
            s += gravitational_interaction(cluster[i], cluster[star_index])
    return s


def centroid(cluster):
    min_interaction, min_index = total_gravitational_interaction(cluster, 0), 0
    for i in range(1, len(cluster)):
        tgi = total_gravitational_interaction(cluster, i)
        if tgi < min_interaction:
            min_interaction = tgi
            min_index = i
    return cluster[min_index][0], cluster[min_index][1], cluster[min_index][2]

print("*" * 15, "Test A", "*" * 15)

# Ищем уравнения границ принятия решений
print("Ищем уравнения границ принятия решений")
dec_points = [[(2, 15), (10, 15)]]

for i, p in enumerate(dec_points):
    k, b = kx_plus_b(p[0], p[1])
    print(f"Граница {i}: k = {k}, b = {b}")

# Считываем данные из файла и кластеризуем их
print("Кластеризация")
num_of_clusters = 2
clusters_of_stars = [[] for _ in range(num_of_clusters)]
with open('27_A_17953.txt') as F:
    next(F)
    for line in F:
        x, y, g = list(map(float, line.replace(',', '.').split()))
        # Кластеризация
        if y > 15:
            seg = 0
        else:
            seg = 1
        clusters_of_stars[seg].append([x, y, g])
print(f"Количество кластеров: {num_of_clusters}")
for i, c in enumerate(clusters_of_stars):
    print(f"Кластер {i}: {len(c)} звёзд")

# Ищем центроиды
print("Начинаем поиск центроидов")
centroids = [ centroid(cl)  for cl in clusters_of_stars ]
for i, cnt in enumerate(centroids):
    print(f"Центроид {i+1}: x = {cnt[0]} y = {cnt[1]} g = {cnt[2]}")

# Ищем центроид с максимальным гравитационным взаимодействием и ответ
max_gravity_centroid = max(centroids, key=lambda c: c[2])
print(f"Центроид с максимальным гравитационным взаимодействием: x = {max_gravity_centroid[0]} ", sep='', end='')
print(f"y = {max_gravity_centroid[1]} g = {max_gravity_centroid[2]} ")

print(f"Ответ: {int(max_gravity_centroid[0] * 1000)} {int(max_gravity_centroid[1] * 1000)}\n\n")

print("*" * 15, "Test B", "*" * 15)

print("Ищем уравнения границ принятия решений")
dec_points = [[(-5, 12), (15, 2)],
              [(-5, 6), (20, 16)]]

for i, p in enumerate(dec_points):
    k, b = kx_plus_b(p[0], p[1])
    print(f"Граница {i}: k = {k}, b = {b}")

# Считываем данные из файла и кластеризуем их
print("Кластеризация")
num_of_clusters = 3
clusters_of_stars = [[] for _ in range(num_of_clusters)]
with open('27_B_17953.txt') as F:
    next(F)
    for line in F:
        x, y, g = list(map(float, line.replace(',', '.').split()))
        # Кластеризация
        if y < x * (-0.5) + 9.5:
            seg = 0
        elif y > 0.4 * x + 8.0:
            seg = 1
        else:
            seg = 2
        clusters_of_stars[seg].append([x, y, g])
print(f"Количество кластеров: {num_of_clusters}")
for i, c in enumerate(clusters_of_stars):
    print(f"Кластер {i}: {len(c)} звёзд")

# Ищем центроиды
print("Начинаем поиск центроидов")
centroids = [ centroid(cl)  for cl in clusters_of_stars ]
for i, cnt in enumerate(centroids):
    print(f"Центроид {i+1}: x = {cnt[0]} y = {cnt[1]} g = {cnt[2]}")

# Ищем центроид с максимальным гравитационным взаимодействием и ответ
max_gravity_centroid = max(centroids, key=lambda c: c[2])
print(f"Центроид с максимальным гравитационным взаимодействием: x = {max_gravity_centroid[0]} ", sep='', end='')
print(f"y = {max_gravity_centroid[1]} g = {max_gravity_centroid[2]} ")

print(f"Ответ: {int(max_gravity_centroid[0] * 1000)} {int(max_gravity_centroid[1] * 1000)}\n\n")