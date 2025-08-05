import matplotlib.pyplot as plt
import random

x = [random.randint(1,20) for _ in range(10)]
y = [random.randint(1,200) for _ in range(10)]

plt.scatter(x,y)
plt.show()