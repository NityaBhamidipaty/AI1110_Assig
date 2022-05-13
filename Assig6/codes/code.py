#Name: Nitya Seshagiri Bhamidipaty
#Rollno. cs21btech11041
#NCERT Class 12 chapter 13 Example 29

'''Two cards are drawn simultaneously (or suc-
cessively without replacement) from a well
shuffled pack of 52 cards. Find the mean,
variance and standard deviation of the number
of kings'''

from cmath import sqrt
from scipy import stats
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from math import comb

#therectical probability
pr0 = comb(48,2)/comb(52,2) #no king
pr1 = comb(4,1)*comb(48,1)/comb(52,2) #one king
pr2 = comb(4,2)/comb(52,2) # two kings
print("The theoretical probability of drawing zero kings is", pr0)
print("The theoretical probability of drawing one king is",pr1)
print("The theoretical probability of drawing two kings is",pr2)

#experimental probability
N = 1000 #sample size
s = np.random.randint(1,53,size=(N,2))
#lets say 1,2,3,4 are kings
k = s.flatten()
#where ever 1,2,3 or 4 replace with 1; 0 otherwise
#1's represent kings, 0's other cards (not king) 
l = np.where(np.logical_or(np.logical_or(k == 1,k == 2) ,np.logical_or(k == 3 ,k == 4) ), 1, 0)
l = np.resize(l,(N,2))

pr_0 = np.count_nonzero((l == (0,0)).all(axis=1))
print("The experimental probability of no king ", pr_0/N)
pr_1 = np.count_nonzero((l == (0,1)).all(axis=1)) + np.count_nonzero((l == (1,0)).all(axis=1))
print("The experimental probability of one king", pr_1/N)
pr_2 = np.count_nonzero((l == (1,1)).all(axis=1))
print("The experimental probability of two kings", pr_2/N)

#calculating mean, variance and standard deviation
xk = np.array([0,1,2])
pk = np.array([188/221,32/221,1/221]) ##can replace with pr0,pr1,pr2

mean = np.sum(np.multiply(xk,pk))
temp = np.sum(np.multiply(pk,np.multiply(xk,xk)))
Var = temp - mean**2
dev = sqrt(Var)

#Let rv X represent the number of kings drawn
print("The mean of X is", mean)
print("The variation of X is",Var)
print("The standard deviation of X is",dev)

#Plotting PMF of X
X = np.array([0,1,2])
Y = np.array([188/221,32/221,1/221])
Z = np.cumsum(Y)

X_cdf = np.array([0,1,2])
Y_cdf = np.array([188/221,220/221,221/221])

#Array for ticks
t = np.array([-1,0,1,2,3])

#pmf
plt.subplot(1,2,1)
plt.xlabel('X')
plt.ylabel('PMF')
plt.xticks(t)
plt.grid()
plt.stem(X, Y, linefmt='k--', markerfmt='ko',basefmt='k-')

#plotting CDF

plt.subplot(1,2,2)
plt.stem(X,Z,linefmt='k--',markerfmt='ko',basefmt='k-')
plt.stem(X_cdf,Y_cdf,linefmt='k--',markerfmt='ko',basefmt='k-')
plt.xlabel('X')
plt.ylabel('CDF')
plt.xticks(t)
plt.grid()
plt.tight_layout()
plt.savefig('../figures/plot.png')

