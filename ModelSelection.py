import math
import scipy.optimize as so
data = np.loadtxt('./data/Modelselection.txt')
x,y = data.T
ad_dif = y[1:]-y[:-1]
sigma = np.std(ad_dif)/math.sqrt(2)

def func(fitc,xx):
    f1 = fitc[0]*np.sin(fitc[6]*xx-fitc[1])+fitc[4]
    f2 = fitc[2]*np.sin(fitc[7]*xx-fitc[3])+fitc[5]
    return f1+f2

def fun(c):
    return (func(c,x)-y)/sigma

fitc,b = so.leastsq(fun,[10,400,10,700,15,15,2*np.pi/500,2*np.pi/500])
plt.scatter(x,y,s=2)
plt.plot(x,func(fitc,x),lw=4)
plt.xlim([0,1000])