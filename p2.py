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
players = list(data.keys())
scores = list(data.values())
print(players)
font1 = {"family": "serif", "color": "darkred", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
plt.barh(players, scores)
plt.title("Total Scores of Royal challengers players", fontdict=font1)
plt.xlabel("Players", fontdict=font2)
plt.ylabel("Scores", fontdict=font2)
plt.show()
