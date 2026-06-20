eps_radius = 1

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def sum_of_dist(cluster, index):
    return sum([dist(cluster[index], p) for p in cluster])


def anticentroid(cluster):
    dists = [(sum_of_dist(cluster, i), cluster[i]) for i in range(len(cluster))]
    return max(dists, key=lambda x: x[0])

print("*" * 15, "Test B", "*" * 15)

with open('27B_21223.txt') as F:
    points = [list(map(float, line[:-1].split())) for line in F]
    clusters = []
    while points:

        # создаём новый кластер
        new_cluster = [points.pop()]

        # для каждой точки из нового кластера
        for p1 in new_cluster:

            # рассматриваем её соотношение с другими точками
            for p2 in points:

                # если между ними расстояние меньше эпсилон-радиуса
                if dist(p1, p2) < eps_radius and p1 != p2:

                    # добавляем точку в наш кластер
                    new_cluster.append(p2)

                    # удаляем её из общего списка точек
                    points.remove(p2)

        # добавляем новый кластер в список кластеров
        clusters.append(new_cluster)


for i, cl in enumerate(clusters):
    print(f"Кластер {i+1}: {len(cl)} точек")


anticentroids = [anticentroid(cl) for cl in clusters if len(cl) > 19]

for i, antcnt in enumerate(anticentroids):
    print(f"Антицентроид {i+1}: dist = {antcnt[0]} x = {antcnt[1][0]} y = {antcnt[1][1]}")

ans_antic = max(anticentroids, key=lambda x: x[0])

print(f"Искомый антицентроид: сумма расстояний = {ans_antic[0]}, x = {ans_antic[1][0]}, y = {ans_antic[1][1]}" )

print(f"Ответ: {int(abs(ans_antic[1][0] * 10000))} {int(abs(ans_antic[1][1]* 10000))}" )