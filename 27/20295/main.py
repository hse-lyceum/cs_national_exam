def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def points_in_one(point, cluster):
    return [p for p in cluster if dist(point, p) < 1]

def density(cluster):
    p_in_one = [len(points_in_one(p, cluster)) for p in cluster]
    return sum(p_in_one) / len(cluster)


def clusterize(path, eps = 1):
    clusters, points = [], []

    # считываем точки из файла
    with open(path) as F:
        points = [list(map(float, line.split())) for line in F]

    while points:

        # новый кластер
        cluster = [points.pop()]

        # для каждой точки в кластере
        for p1 in cluster:

            # проверяем каждую некластеризованную точку
            for p2 in points:

                # если она из того же кластера, добавляем её в кластер
                # и удаляем из списка некластеризованных точек
                if dist(p1, p2) < eps:
                    cluster.append(p2)
                    points.remove(p2)

        # новый кластер сформирован, добавляем его в список кластеров
        clusters.append(cluster)
    return clusters

def answer(path, eps = 1):
    clusters = clusterize(path, eps)
    densities = [density(cl) for cl in clusters]
    for i, cl in enumerate(zip(clusters, densities)):
        print(f"Кластер {i + 1}: {len(cl[0])} точек, плотность = {cl[1]}")
    pmin, pavg = min(densities), sum(densities) / len(densities)
    return [int(pmin * 100000), int(pavg * 100000)]


print("Test A:", *answer('27A_20295.txt'), "Test B:", *answer('27B_20295.txt', 0.4))