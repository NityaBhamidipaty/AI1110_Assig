#Ncert class 10 Probability 15.2 example 10
#Name: Nitya Seshagiri Bhamidipaty
#Roll no. cs21btech11041

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import uniform

#plotting the probability density function
x = np.linspace(-1, 3,100) #generating 100 linearly spaced numbers in [-1,3]
y = uniform.pdf(x, 0, 2)   #generating values for uniform pdf (lower bound 0 and range 2)
plt.grid(True)
plt.title('PDF of X')
plt.xlabel('Random Variable X')
plt.ylabel('f(x)')
plt.plot(x, y) 
plt.savefig('./figs/plot.png')

#calculating the probability that the music stops before 0.5 minutes

pr = uniform.cdf(x=0.5, loc=0, scale=2) - uniform.cdf(x=0, loc=0, scale=2)
print('The probability that the music stops before 0.5 minutes is',pr)

#experimental probability

sample_space = np.random.uniform(0.0,2.0,10000)
pr = sample_space[sample_space <= 0.5 ]
print('The experimental probability is',(pr.size)/(sample_space.size))