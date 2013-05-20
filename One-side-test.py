"""
For an exponentially distributed test statistic with mean μ (under the null hypothesis), when is the the null hypothesis disproved with p < 0.01 for a one-sided test? for a two-sided test?
For any exponentially distributed test statistic with mean μ, just initialize the variable 'mean' equal to m. The next example is run with m = 0(For sanity check)
"""

import scipy.stats as sc
import numpy as np

mean =0

r = sc.expon(loc = mean)
x = np.linspace(-1,1)
plt.plot(x,r.pdf(x))

#One sided
print "One sided: " +str(r.ppf(0.01))
#Two sided
print "Two sided:"
print "left: " + str(r.ppf(0.005))
#right tail
print "right: " +str(r.ppf(1-0.005))

One sided: 0.0100503358535
Two sided:
left: 0.00501254182354
right: 5.29831736655