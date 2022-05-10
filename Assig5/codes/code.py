#Name: Nitya Seshagiri Bhamidipaty
#Rollno. cs21btech11041
#NCERT Class 11 chapter 16 miscellaneous q8

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#read raw data from excel sheet
df = pd.read_excel(r'data.xlsx')

sno = np.array(df['S.No.'])
gender = np.array(df['Sex'])
age = np.array(df['Age in years']) 

sno = sno[np.logical_and((age<=35) , (gender == 'F'))]

#experimental probability
samplespace = 1000
x = np.random.randint(1,high = 6,size = samplespace)
y = np.array([u for u in x if u in sno])

print("The experimental probability of the spokesperson of either being a male or over 35 years is ",end=None)
print(format((1 - y.size/samplespace),".3f"))

#theoretical probability
age = age[gender == 'F']
age = age[age<=35]
pr = 1 - age.size/gender.size
print("The theoretical probability of the spokesperson of either being a male or over 35 years is " , pr)

#Plotting PMF and CDF of X
X = np.array([0,1])
Y = np.array([3/5,2/5])
Z = np.cumsum(Y)


X_cdf = np.array([0,1])
Y_cdf = np.array([3/5,5/5])

#Arrays for ticks
t = np.array([-1, 0, 1, 2])

#Plotting the PMF
plt.subplot(2,2,1)
plt.xlabel('X')
plt.ylabel('PMF')
plt.xticks(t)
plt.grid()
plt.stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(2,2,2)
plt.stem(X, Z, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.stem(X_cdf, Y_cdf, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('X')
plt.ylabel('CDF')
plt.xticks(t)
plt.grid()
plt.tight_layout()

#Plotting PMF and CDF of Y

X2 = np.array(df['Age in years'])
X2 = np.sort(X2)
Y2 = np.array([1/5,1/5,1/5,1/5,1/5])
Z2 = np.cumsum(Y2)

X_cdf2 = np.array(df['Age in years'])
X_cdf2 = np.sort(X_cdf2)
Y_cdf2 = np.array([1/5,2/5,3/5,4/5,5/5])

#Arrays for ticks
t2 = np.array([28,30,32,40,42,44,46,48])

#Plotting the PMF
plt.subplot(2,2,3)
plt.xlabel('Y')
plt.ylabel('PMF')
plt.xticks(t2)
plt.grid()
plt.stem(X2, Y2, linefmt='k--', markerfmt='ko', basefmt='k-')

#Plotting the CDF
plt.subplot(2,2,4)
plt.stem(X2, Z2, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.stem(X_cdf2, Y_cdf2, linefmt='k--', markerfmt='ko', basefmt='k-')
plt.xlabel('Y')
plt.ylabel('CDF')
plt.xticks(t2)
plt.grid()
plt.tight_layout()
plt.savefig('../figures/pdfy.png')


