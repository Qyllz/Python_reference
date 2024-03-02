import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode = [0.2, 0, 0, 0]
# using explode separates the pie ising the index number
colors = ["red", "#ffc0cb", "b", "#4CAF50"]

plt.pie(y, labels=labels, startangle=90, explode=explode, colors=colors)
plt.legend(title="Fruits")
plt.show()
