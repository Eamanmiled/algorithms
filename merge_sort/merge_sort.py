import random

data_points = []
amt_data_points = random.randint(5, 20)
i = 0
while i != amt_data_points:
    data_points.append(random.randint(0, 9999))
    i += 1
print("There is", amt_data_points, "data points")

# -algo-
def swapPos(list, in1, in2):
    list[in1], list[in2] = list[in2], list[in1]
    return list


def sorting(A, B):
    output = A + B
    i = 0
    while i < len(output):
        j = i + 1
        while j < len(output):
            if output[i] > output[j]:
                swapPos(output, i, j)
                j = i + 1
            j += 1
        i += 1
    print(output)


data_points2 = [2, 4]

sorting(data_points, data_points2)

# copy_lis = data_points
# # left
# mid = (len(copy_lis) - 1) // 2
# i = 0
# while i != mid

