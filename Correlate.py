"""
Suppose you want to get a feel for what a linear correlation r = 0.3 (say) looks like. How would you generate a bunch of points in the plane with this value of r? Try it. Then try for different values of r. As r increases from zero, what is the smallest value where you would subjectively say "if I know one of the variables, I pretty much know the value of the other"?
"""
import matplotlib.pyplot as plt

v=0.3
mean = [0,0]
cov = [[1,v],[v,1]] # diagonal covariance, points lie on x or y-axis

x,y = np.random.multivariate_normal(mean,cov,1000).T
plt.plot(x,y,'x'); plt.axis('equal'); plt.show()


r = np.corrcoef(x,y)