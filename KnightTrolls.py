import random
"""
1. Simulate the Knight/Troll/Gnome problem.
We simulated a knight approaching a bridge, and measuring the probabilities that the knight crosses safely
without capturing a creature
after capturing a creature
if he only crosses the bridge if he captured a troll
if he only crosses the bridge if he captured a gnome
This produced the following result, which matches all expected probabilities.
"""
data0 = []
data1 = []
data2 = []
data3 = []
safe0 = 0
safe1 = 0
safe2 = 0
safe3 = 0
attempts1 = 0
attempts2 = 0
for i in range(100000):
    x = random.random()
    if x < 1.0/5:
        t = 2
    elif x < 2.0/5:
        t = 1
    else:
        t = 0
        
    # What if we cross without a capture
    if t == 0:
        safe0 += 1
    data0.append(safe0*1.0/(i+1))

    # Capture will be True if the kinght has captured a troll
    capture = random.random() < t/5.0
    if capture:
        # Cross if captured a troll
        t -= 1
        if t == 0:
            safe1 += 1
            safe3 += 1
        #continue
        attempts1 += 1
        data1.append(safe1*1.0/attempts1)
    else:
        # Cross if captured a gnome
        if t == 0:
            safe2 += 1
            safe3 += 1
        attempts2 += 1
        data2.append(safe2*1.0/attempts2)
    data3.append(safe3*1.0/(i+1))

plot(data3, label="Without capture, %f" % data3[-1])
plot(data0, label="With capture, %f" % data0[-1])
plot(data1, label="Only if captured troll, %f" % data1[-1])
plot(data2, label="Only if captured gnome, %f" % data2[-1])
legend(loc='best')
ylabel('% Safe crossings')
print data0[-1], data1[-1], data2[-1], data3[-1]
# If we cross when we capture a troll (and don't otherwise),
#   we cross safely with probability .33, matches lecture
# If we cross when we capture a gnome (and don't otherwise),
#   we cross safely with probability .68, matches exercise