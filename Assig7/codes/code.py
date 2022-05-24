# Papolous chapter 2 Example 29 CHECK!!
# Name: Nitya Seshagiri Bhamidipaty
# Roll no. cs21btech11041

import numpy as np
from matplotlib import pyplot as plt

#t_0 = 10
# just assuming some t_0 value

# Plotting the Probability density function
x = np.linspace(0, 10, 100)
y = np.exp(-1*x)
plt.grid(True)
plt.title('PDF of t')
plt.xlabel('Time (t)')
plt.ylabel('Probability Density Function')
plt.plot(x, y)
plt.savefig('../figures/plot.png')
# plt.subplot(x,y)
