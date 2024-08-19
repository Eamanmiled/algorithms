import random

# In this algorithm I will select subsets of N and search
# to see which subset has the highest sum val in len of list
# using python

data_points = []
amt_data_points = random.randint(5, 20)
i = 0
while i != amt_data_points:
    data_points.append(random.randint(0, 9999))
    i += 1
print("There is", amt_data_points, "data points")
inp = input("How Long would you like your subset to be? ")
while True:
    if inp.isdigit():
        inp = int(inp)

        if inp > amt_data_points:
            print("thats too big of a num???")

        else:
            break
    else:
        print("thats not a numeric number i.e 1 or 2???")
    inp = input("try again :")
# -----------------
# actual algorithm is below all above is for random and interactivity
# -----------------
largest_sum = 0
i = 0
while not i + inp > len(data_points):
    print(data_points[i: i + inp])
    if sum(data_points[i: i + inp - 1]) > largest_sum:
        largest_sum = sum(data_points[i: i + inp - 1])
        i += 1
    else:
        i += 1

print(data_points)
print(largest_sum)
