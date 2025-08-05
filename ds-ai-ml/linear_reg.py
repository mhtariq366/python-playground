import matplotlib.pyplot as plt
import random
from scipy import stats

def get_y(x):
    return m * x + c

x = [random.randint(1,20) for _ in range(10)]
y = [random.randint(1,200) for _ in range(10)]

m, c, r, p, std_err = stats.linregress(x, y)

lin_model = list(map(get_y, x))

plt.scatter(x,y)
plt.plot(x, lin_model)
plt.show()
