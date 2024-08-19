import random

data_points = []
amt_data_points = random.randint(5, 20)
for _ in range(amt_data_points):
    data_points.append(random.randint(0, 9999))
print("There are", amt_data_points, "data points")
print("Og data points:", data_points)

# -algo-


def swapPos(list, in1, in2):
    list[in1], list[in2] = list[in2], list[in1]
    return list


def sorting(A, B): # left and right
    output = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]: # if the left list index is smaller
            output.append(A[i])
            i += 1
        else: # if the right list index is smaller
            output.append(B[j])
            j += 1
# once it hits the end slap rest of other list on the end
    output.extend(A[i:])
    output.extend(B[j:])

    return output


def dividing(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis) // 2
    left_half = dividing(lis[:mid]) # Recursively divide the list into two halves
    right_half = dividing(lis[mid:])
    return sorting(left_half, right_half) # then merge


sorted_data_points = dividing(data_points)
print("Sorted data points from lowest to highest:", sorted_data_points)
