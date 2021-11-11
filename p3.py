import csv

from matplotlib import pyplot as plt

data = {}
with open("/home/gowthami/project1/umpires.csv", "r") as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)
    for i in csv_read:
        c = i[1]
        if c != " India":
            print(c)
            if c in data:
                data[c] += 1
            else:
                data[c] = 1

country = list(data.keys())
no_of_umpires = list(data.values())
print(sum(no_of_umpires))
font1 = {"family": "serif", "color": "darkred", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}
plt.barh(country, no_of_umpires)
plt.title("No of Umpires from each country", fontdict=font1)
plt.xlabel("Country", fontdict=font2)
plt.ylabel("No of Umpires", fontdict=font2)
plt.show()
