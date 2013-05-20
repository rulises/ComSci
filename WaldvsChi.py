import itertools
import mathplotlib.pyplot as plt

def chisquare(table):
        N = np.sum(table)
        rowsums = [np.sum(x) for x in table]
        colsums = [np.sum(x) for x in table.T]
        n = np.outer(rowsums,colsums)*1.0/N
        return np.sum( (table - n )**2/n)

def wald(table):
        N = np.sum(table)
        rowsums = [np.sum(x) for x in table]
        colsums = [np.sum(x) for x in table.T]
        p1= table[0][0]/colsums[0]
        p2=table[0][1]/colsums[1]
        p= rowsums[0]/N
        return (p1-p2)/np.sqrt(p*(1-p)*(1.0/rowsums[0]+1.0/rowsums[1]))

N,m,n=14,2,2
position = [posi for posi in range(N+m*n-1)]
walds = []
chis = []
stars=[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for x in permutations(balls):
    i = 0
    t = [0,0,0,0]
    for s in stars:
          if(s ==0):
                i+=1
          t[i]+=1 
    table = np.array([[t[0],t[1]],[t[2],t[3]]])
    walds.append(wald(table))
    chis.append(chisquare(table))
print len(waltl)
plt.plot(chis,walds)