import random
data_points = []
amt_data_points = random.randint(5, 20)
for _ in range(amt_data_points):
    data_points.append(random.randint(0, 9999))
print("There are", amt_data_points, "data points")
print("Og data points:", data_points)


def swap(lis, p1, p2):
    lis[p1], lis[p2] = lis[p2], lis[p1]
    return lis

# -algo-


i = 0
while i < len(data_points):
    j = i + 1
    while j < len(data_points):
        if data_points[i] > data_points[j]:
            swap(data_points, i, j)
            j = i + 1
        j += 1
    i += 1

print("Sorted Data Points:", data_points)
