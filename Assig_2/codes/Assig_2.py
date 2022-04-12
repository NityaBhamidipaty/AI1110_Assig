#Nitya Seshagiri Bhamidipaty
#cs21btech11041
#icse 12th  2018 13(a)

import sympy as smp

x = smp.symbols('x',real = True)
u = smp.symbols('u',real = True)
exp = (x-1)/smp.sqrt(x**2-x)
#(x-1)/smp.sqrt(x**2-x) = 0.5(2x-1)/smp.sqrt(x**2-x) - 1/smp.sqrt(4*x**2-4*x)
exp_1 = (2*x-1)/smp.sqrt(x**2-x)
r = 0.5*smp .integrate(exp_1,x) #first part
#1/smp.sqrt(4*x**2-4*x) = 1/smp.sqrt((2*x-1)**2-1);u = 2*x-1
exp_2 = 1/smp.sqrt((2*x-1)**2-1)
exp_2 = exp_2.replace((2*x-1),u)
s = 0.5*smp.integrate(exp_2,u)
s = s.replace(u,2*x-1)#second part
print(r - s)
