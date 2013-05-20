def contingency_table(table):
    col_sums = table.sum(axis=0)
    row_sums = table.sum(axis=1)
    N = table.sum()
    expected = np.outer(row_sums, col_sums) / float(N)
    chisqs = (table - expected)**2 / expected
    chisq = chisqs.sum()
    dofs = np.prod(table.shape) - sum(table.shape) + 1
    p_val = 1 - scipy.chi2(dofs).cdf(chisq)
    return chisq, p_val
def perm_test(table):
    col_sums = table.sum(axis=0)
    row_sums = table.sum(axis=1)
    N = table.sum()
    cols = []
    rows = []
    count = 0
    for i in col_sums:
        for x in range(0, int(i)): 
            cols.append(count)
        count += 1
    count =0
    for i in row_sums:
        for x in range(0, int(i)): 
            rows.append(count)
        count += 1
    #print zip(cols, rows)
    rows = numpy.random.permutation(rows)
    n = zip (rows,cols)
    newtable = numpy.zeros((len(table),len(table[0])))
    for i,j in n:
        newtable[i][j] += 1
    return newtable
import matplotlib.pyplot as plt
table = np.array([[1.0, 1.0, 13.0],
                  [16.0, 4.0, 15.0], 
                  [45.0, 32.0, 80.0]])
newTable = perm_test(table)
print "chisq ", contingency_table(table)[0]
print "pvalue ", contingency_table(table)[1]

chis = []
for i in range(0,1000000):
    newTable = perm_test(table)
    chis.append(contingency_table(newTable)[0])
plt.hist(chis, bins =40)