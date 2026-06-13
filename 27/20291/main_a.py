def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def cluster_diameter(cluster):
    max_dist = 0
    for i in range(len(cluster)):
        for j in range(len(cluster)):
            d = dist(cluster[i], cluster[j])
            max_dist = max(max_dist, d)
    return max_dist


def rectangle_by_diag(p1, p2):
    return [[p1[0], p1[1]], [p1[0],p2[1]], [p2[0], p2[1]], [p2[0], p1[1]]]


def in_rectangle(p, r):
    min_x = min([r[i][0] for i in range(4)])
    max_x = max([r[i][0] for i in range(4)])
    min_y = min([r[i][1] for i in range(4)])
    max_y = max([r[i][1] for i in range(4)])
    return min_x < p[0] < max_x and min_y < p[1] < max_y

print("*" * 15, "Part A", "*" * 15)

# Диагонали прямоугольников-решений
cluster_diags = [[[0, 0],  [-3, 4]],
                 [[5, 2],  [2, 5]],
                 [[-2, 0],  [1, -5]],
                 [[3, 2],  [8, -3]]]

number_of_clusters = len(cluster_diags)
clusters = [[] for _ in range(number_of_clusters)]
print(f"Количество кластеров: {number_of_clusters}")
cluster_full_rectangles = [rectangle_by_diag(r[0], r[1]) for r in cluster_diags]
print("Вершины прямоугольников-решений:")
for i, cl in enumerate(cluster_full_rectangles):
    print(f"Прямоугольник {i + 1}: {cl}")

# Чтение данных и кластеризация
with open('27A_20291.txt') as F:
    for line in F:
        x, y = map(float, line.split())

        # Кластеризация
        for i in range(len(cluster_full_rectangles)):
            if in_rectangle([x, y], cluster_full_rectangles[i]):
                clusters[i].append([x, y])
                break

print("Кластеры:")
for i, cl in enumerate(clusters):
    print(f"Кластер {i}: {len(cl)} звёзд")

cluster_diameters = [cluster_diameter(cl) for cl in clusters]
print("Диаметры кластеров:")

for i, cld in enumerate(cluster_diameters):
    print(f"Кластер {i}: диаметр = {cld}")

answer = [int(min(cluster_diameters) * 100000),
          int(sum(cluster_diameters) / number_of_clusters * 100000)]

print("Ответ:", *answer)