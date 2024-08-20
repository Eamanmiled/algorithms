import random

data_points = []
amt_data_points = random.randint(5, 20)
for _ in range(amt_data_points):
    data_points.append(random.randint(0, 9999))
print("There are", amt_data_points, "data points")
print("Og data points:", data_points)


def swap(lis, pos, pos2pop, var):
    lis.insert(pos, var)
    lis.pop(pos2pop)
    return lis


# -algo-
i = 1
while i < len(data_points):
    j = 0
    while j < i:
        if data_points[i] < data_points[j]:
            swap(data_points, j, i+1, data_points[i])
        j += 1
    i += 1
print("sorted data points:", data_points)
