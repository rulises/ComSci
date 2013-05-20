"""
• Nsequentialtrials each with outcomes 0 or 1
– trial number 1 is Bernoulli with probability p (of outcome = 1)
– trials number 2:N, do this:
• with probability q,replicate immediately previous outcome
• with probability (1‐q), Bernoulli outcome with probability p
– if n = (sumofthe trials), we wantto compute P(n|N,p,q)
• note that P(n|N,p,0)isthe binomial bin(n|N,p)
• and thatthemean <n> =Np isindependent of q
• Simulation subteam: compute P(n,12,0.8,0.2)for n=0:12
– can you get P(0,12,0.8,0.2)to an accuracy ≈0.1%?
"""
N = 12
trials = [0]*N
p = .8
q = .2
n = 13
bins = [0]*n
runs = 10000000
for runs in range(0,runs):
    #– trial number 1 is Bernoulli with probability p (of outcome = 1)
    trials[0]= 1 if random.random() < p else 0
    for x in range(1,N):
        trials[x]= trials[x-1] if random.random() < q else 1 if random.random() < p else 0
    #– if n = (sum of the trials), we want to compute P(n|N,p,q)
    bins[sum(trials)] += 1
bins = [float(x)/float(runs) for x in bins]