import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Nigga", "NIgga", "NIgGa", "NIgGA"])
y = np.array([3, 8, 1, 10])

font1 = {'family': 'serif', 'color': 'black', 'size': 20}

# plt.barch(x, y) if you want the bar to be horizontal
plt.bar(x, y, color='#ffc0cb')
plt.title("Bubble Gum Pink", fontdict=font1)
plt.show()
