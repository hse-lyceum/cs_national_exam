def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def rect_by_diag (p1, p2):
    return [[p1[0], p1[1]], [p1[0], p2[1]], [p2[0], p2[1]], [p2[0], p1[1]]]


def in_rectange(p, r):
    xmin = min([r[0][0], r[1][0], r[2][0], r[3][0]])
    xmax = max([r[0][0], r[1][0], r[2][0], r[3][0]])
    ymin = min([r[0][1], r[1][1], r[2][1], r[3][1]])
    ymax = max([r[0][1], r[1][1], r[2][1], r[3][1]])
    return xmin < p[0] < xmax and ymin < p[1] < ymax


def points_in_neighborhood(p_index, cluster):
    return sum([1 for i in range(len(cluster)) if i != p_index and dist(cluster[p_index], cluster[i]) <= 1])


def aim_point(cluster):
    max_index, max_points = 0, points_in_neighborhood(0, cluster)
    for i in range(1, len(cluster)):
        pn = points_in_neighborhood(i, cluster)
        if pn > max_points:
            max_points = pn
            max_index = i
        elif pn == max_points:
            if cluster[i][0] > cluster[max_index][0]:
                max_index = i
    return cluster[max_index]

print("*" * 15, "Test A", "*" * 15)

rect_diagonals = [ [[-3, 3], [0, 0]],
                   [[-2, 0], [2, -4]],
                   [[2, 5], [5, 2]],
                   [[3, 2], [8, -3]] ]
number_of_clusters = len(rect_diagonals)
print(f"Количество кластеров: {number_of_clusters}")

cluster_borders = [rect_by_diag(p1, p2) for p1, p2 in rect_diagonals]
print("Границы кластеров:")
for i, cl in enumerate(cluster_borders):
    print(f"Кластер {i}: {cl}")

clusters = [[] for _ in range(number_of_clusters)]
with open('27A_20293.txt') as F:
    for line in F:
        x, y = map(float, line.split())
        for i in range(number_of_clusters):
            if in_rectange([x, y], cluster_borders[i]):
                clusters[i].append([x, y])
                break

print("Кластеры:")
for i, cl in enumerate(clusters):
    print(f"Кластер {i}: {len(cl)} точек")

aim_points = [aim_point(cl) for cl in clusters]
print("Точки наведения:")
for i, ap in enumerate(aim_points):
    print(f"Кластер {i}: x = {ap[0]}, y = {ap[1]}")

answer_a = [int(abs(sum([p[0] for p in  aim_points]) / number_of_clusters) * 100000),
            int(abs(sum([p[1] for p in  aim_points]) / number_of_clusters) * 100000)
           ]
print(*answer_a)

