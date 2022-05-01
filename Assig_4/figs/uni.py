#
# 
#Uniform Distribution describes an experiment where there is an random outcome that lies between certain bounds. The bounds of the outcome are defined by the parameters, a and b, which are the minimum and maximum values. All intervals of the same length on the distribution has equal probability.
#
#The probability density function (pdf) of uniform distribution is defined as:
#
#Uniform Distribution
#Where, a and b are lower and upper boundaries of output interval respectively.
#
#An uniform distribution has mean (a+b)/2 and variance (b-a)2/12.
#
#
#
# 
#
#The cumulative distribution function (cdf) evaluated at x, is the probability that the random
# variable (X) will take a value less than or equal to x. The cdf of uniform distribution is defined as:
#Uniform Distribution
#The scipy.stats.uniform contains all the methods required to generate and work with an uniform distribution. 
#The most frequently methods are mentioned below:

#Syntax
#scipy.stats.uniform.pdf(x, loc=0, scale=1)
#scipy.stats.uniform.cdf(x, loc=0, scale=1)
#scipy.stats.uniform.ppf(q, loc=0, scale=1)
#scipy.stats.uniform.rvs(loc=0, scale=1, size=1)
#Parameters
#x	Required. Specify float or array_like of floats representing random variable.
#q	Required. Specify float or array_like of floats representing probabilities.
#loc	Optional. Specify lower boundary of the output interval. Default is 0.0.
#scale	Optional. Specify scale of the output. Upper boundary of the output interval will be (loc + scale). Must be non-negative. 
#Default is 1.0.
#size	Optional. Specify output shape.

#uniform.pdf()
#The uniform.pdf() function measures probability density function (pdf) of the distribution.

from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

#creating an array of values between
#-3 to 8 with a difference of 0.1
x = np.arange(-3, 8, 0.1)
   
y = uniform.pdf(x, 0, 5)
   
plt.plot(x, y) 
plt.show()
