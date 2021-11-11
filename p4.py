import csv

from matplotlib import pyplot as plt

data = {}
l = []
with open("/home/gowthami/project1/matches.csv", "r") as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)
    for i in csv_read:
        y = i[1]
        t1 = i[4]
        t2 = i[5]
        if t1 not in l:
            l.append(t1)
        if t2 not in l:
            l.append(t2)
        if y in data:

            if t1 in data[y]:

                data[y][t1] += 1
            else:
                data[y][t1] = 1
            if t2 in data[y]:

                data[y][t2] += 1
            else:
                data[y][t2] = 1
        else:
            data[y] = {t1: 1, t2: 1}
k = list(data.keys())
k.sort()
m = []

for i in k:
    f = []
    for j in l:
        if j in data[i]:
            f.append(data[i][j])
        else:
            f.append(0)
    m.append(f)
z = []
clr = [
    "lime",
    "purple",
    "black",
    "green",
    "olive",
    "red",
    "yellow",
    "blue",
    "teal",
    "aqua",
    "navy",
    "grey",
    "fuchsia",
    "maroon",
]
p = 0
for i in range(len(m[0])):
    temp = []
    for j in range(len(m)):
        temp.append(m[j][i])
    if z == []:
        plt.bar(k, temp, color=clr[p])
        p += 1
        z = temp
    else:
        plt.bar(k, temp, bottom=z, color=clr[p])
        p += 1
        for i in range(len(temp)):
            z[i] = z[i] + temp[i]
for i in k:
    print(i, data[i])
plt.xlabel("Year")
plt.ylabel("No of games played by team")
plt.legend(l)
plt.title("No of games played by team by season")
plt.show()
