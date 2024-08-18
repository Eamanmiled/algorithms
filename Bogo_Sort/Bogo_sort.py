import random

lis = []
n = random.randint(2, 10)
for i in range(n):
    lis.append(random.randint(4, 100))

# --------
# Algo
# --------
try_count = 0
i = 1
while i < len(lis):
    if lis[i] < lis[i - 1]:
        random.shuffle(lis)
        i = 1
        try_count += 1
    else:
        i += 1

print(lis)
print("Bogo_sort ran", try_count, "times")
