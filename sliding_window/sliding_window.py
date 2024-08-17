import random

#In this algorithm I will select subsets of N and search
#to see which subset has the highest sum val in len of list
#using python

data_points = []
amt_data_points = random.randint(5, 20)

i = 0
while i != amt_data_points:
    data_points.append(random.randint(0, 9999))
    i += 1
print("There is", amt_data_points, "data points")
len_of_input = int(input("How Long would you like your subset to be? "))
if len_of_input > amt_data_points:
    print("that's larger then the amount of data points available silly")
    len_of_input = int(input("Lets try this again or there will be a error as its late and cba to implement a fix: "))

# -----------------
# actual algorithm is below all above is for random and interactivity
# -----------------
largest_sum = 0
i = 0
while i + len_of_input != len(data_points):
    if sum(data_points[i: i + len_of_input - 1]) > largest_sum:
        largest_sum = sum(data_points[i: i + len_of_input - 1])
        i += 1
    else:
        i += 1

print(largest_sum)
