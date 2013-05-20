"""
K-clustering
"""
import matplotlib.pyplot as plt
# n data points
# into
# k clusters
def kmean(n, k):
    #First Guesses
    s = [[] for x in range(0,k)]
    means = [n[x*len(n)/k] for x in range(0,k) ]
    done =0
    for j in range(0,10):
        #print means
        for x in n:
            counter = 0
            nearest = 0
            for m in means:
                if(((x[0]-m[0])**2+(x[1]-m[1])**2)**.5 < ((x[0]-means[nearest][0])**2+(x[1]-means[nearest][1])**2)**.5 ):
                    nearest = counter
                counter += 1
            s[nearest].append(x)
        new_means = [[] for x in range(0,k)]
        counter = 0
        for c in s:
            sy = 0 
            sx = 0
            for x, y in c:
                sy+=y
                sx+=x
            new_means[counter] = [sx/len(c) , sy/len(c)]
            counter+=1
        counter =0
        
        for m in means:
            if(((new_means[counter][0]-m[0])**2+(new_means[counter][1]-m[1])**2)**.5==0):
                #converge, so break
                done =1
                break
            else:
                #Update means
                means[counter][1] = new_means[counter][1]
                means[counter][0] =new_means[counter][0]
            counter+=1
        if done == 1:
            break
            
     #Plot
            
    for c in s:
        acolor = next(color)
        plt.plot([x for x,y in c ],[y for x,y in c ],'bo',color = acolor)
    
color = get_color()
kmean(data, 8)
color = get_color()
kmean(data, 3)