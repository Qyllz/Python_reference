import numpy as np
import matplotlib.pyplot as plt
# graphing
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# labels and font
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
plt.title("Sports Watch Data", loc='center', fontdict= font1)
plt.xlabel("Average Pulse",fontdict= font2)
plt.ylabel("Calorie Burnable", fontdict= font2)

# plotting
plt.plot(x, y)

# showing the grid
plt.grid()
plt.show()
