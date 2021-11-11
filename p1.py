import csv

from matplotlib import pyplot as plt

data = {}
with open("/home/gowthami/project1/deliveries.csv", "r") as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)
    for i in csv_read:
        t = i[2]
        s = int(i[17])
        if t in data:
            data[t] += s
        else:
            data[t] = s
teams = list(data.keys())
scores = list(data.values())
font1 = {"family": "serif", "color": "darkred", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
plt.barh(teams, scores)
plt.title("Total Scores of Teams", fontdict=font1)
plt.xlabel("Teams", fontdict=font2)
plt.ylabel("Scores", fontdict=font2)

plt.show()
