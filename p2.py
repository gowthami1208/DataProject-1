#Top 10 batsman for Royal Challengers Bangalore
import csv

from matplotlib import pyplot as plt

data = {}
with open("/home/gowthami/project1/deliveries.csv", "r") as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)
    for i in csv_read:
        t = i[2]
        b = i[6]
        s = int(i[17])
        if t == "Royal Challengers Bangalore":
            if b in data:
                data[b] += s
            else:
                data[b] = s
d = sorted(data.values(), reverse=True)
k = {}
for i in d[:10]:
    for j in data:
        if data[j] == i:
            k[j] = i
            break
players = list(k.keys())
scores = list(k.values())
print(players)
font1 = {"family": "serif", "color": "darkred", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
plt.barh(players, scores)
plt.title("Total Scores of Royal challengers players", fontdict=font1)
plt.xlabel("Players", fontdict=font2)
plt.ylabel("Scores", fontdict=font2)
plt.show()
