import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


def counts(x):
    n = np.zeros(10)
    for i in x:
        n[i] += 1
    return n

data = np.loadtxt('data/Gibbs_data.txt')

assignments = sp.binom.rvs(1, 0.5, size =1000)
hist_p = []
rel_p = []
rel_q = []
for it in range(0,1000):
    ps = np.zeros(10)
    qs = np.zeros(10)
    #Count number of digits for p and q
    for i in range(0,1000):
        if assignments[i] == 1: #P
            ps+= counts(data[i])
        else:
            qs+= counts(data[i])
    #Calculate Prob of qs and ps
    ps = ps/sum(ps)
    qs = qs/sum(qs)
    
    hist_p.append(ps)
    
    
    p =1.0
    q =1.0
    #Recalculate the reasssignment
    for i in range(0,1000):
        p = prod([ps[x] for x in data[i]])
        q = prod([qs[x] for x in  data[i]])
        rel = p/(p+q)
        if rel > np.random.uniform():
            assignments[i] = 1
        else:
            assignments[i] = 0
 
plt.hist(hist_p,bins=30)
print hist_p[len(hist_p)-1]