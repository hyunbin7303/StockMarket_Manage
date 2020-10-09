
import numpy as np
import matplotlib.pyplot as plt

N = 3
A_Means = (30,40,50)
B_Means = (50,40,50)
A_Std = (2,3,4)
B_Std = (1,5,2)
ind = np.arange(N)
width = 0.35

P1 = plt.bar(ind, A_Means, width, yerr=A_Std)
P2 = plt.bar(ind, B_Means, width, bottom = A_Means, yerr = B_Std)


plt.ylabel('Values')
plt.title("BAR GRAPH TESTING")
plt.xticks(ind, ("A1", "A2", "A3"))
plt.legend((P1[0], P2[0]), ('AAA', 'BBB'))

plt.show()
