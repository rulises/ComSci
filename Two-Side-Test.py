"""
What is the critical region for a 5% two-sided test if, under the null hypothesis, the test statistic is distributed as Student(0,σ,4)? That is, what values of the test statistic disprove the null hypothesis with p < 0.05? 
"""

import scipy.stats as sc
import numpy as np
[df] =  [4,] * sc.t.numargs
r = sc.t(df)
x = np.linspace(-4,4)
plt.plot(x,r.pdf(x))
 
#left tail
print "left: " +str(r.ppf(0.025))
 
#right tail
print "right: " +str(r.ppf(1-0.025))
left: -2.7764451052
right: 2.7764451052