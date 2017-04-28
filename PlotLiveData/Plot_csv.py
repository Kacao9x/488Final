import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('sample_data_for_kacao.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='Loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Relation between x and y')
plt.legend()
plt.show()

for (item1, item2) in (len(x)/5,len(y)/5):
    print x[item1], y[item2]


