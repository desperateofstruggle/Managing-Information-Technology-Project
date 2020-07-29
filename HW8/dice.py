import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

# control dice times
THORWN_TIMES = 30
dice_1 = np.random.randint(low=1, high=7, size=THORWN_TIMES, dtype='int')
dice_2 = np.random.randint(low=1, high=7, size=THORWN_TIMES, dtype='int')
dice_sum = dice_1 + dice_2

print(dice_1)
print(dice_2)

Y_times = [0] * 11

for it in dice_sum:
    Y_times[it-2] += 1

X = np.arange(2, 13, 1)
X_new = np.linspace(X.min(), X.max(), 30)
Y_smooth = spline(X, Y_times, X_new)
plt.xlabel("Sum")
plt.ylabel("Times")
plt.title("Smooth Curve For Two Dices Thrown " + str(THORWN_TIMES) + " Times")
plt.plot(X_new, Y_smooth)
plt.show()


plt.bar(X, Y_times)
plt.xlabel("Sum")
plt.ylabel("Times")
plt.title("Histogram For Two Dices Thrown " + str(THORWN_TIMES) + " Times")
plt.show()
