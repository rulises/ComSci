"""
Now there areNdoors. You
pick one. Monte then opens
n others, leaving closed
your door along withN‐n‐1
others.
You are offered the chance
to switch to one other door.
Should you switch orstay?
Let’s divide each teaminto two sub‐teams, one to work the problemanalytically,the
other by simulation. You’re allowed to exchange ideas and data between the two
sub‐teams.
Simulation teams:Get answersforspecific cases
N=7 doors: open n=3, or 4, or 5; and N=8 doors: open n=3, 4, or 5.
"""

 def game():
       #states
       picked_notPrize = 1
       picked_prize = 2
       notPicked_notPrize = 3
       notPicked_prize = 4
       opened = 5
   
       n = 3
       bigN = 7
       
       doors = [notPicked_notPrize]*bigN
       #placing prize
       p = randint(0,bigN)
       doors[p] = notPicked_prize
   
       #player picking door
       player_pick = randint(0,bigN)
       if p == player_pick:
           doors[player_pick] = picked_prize
       else:
           doors[player_pick] = picked_notPrize
   
       #Monty opens doors
       opened_doors = 0
   
       while opened_doors < bigN:
           p = randint(0,bigN)
           if doors[p] == notPicked_notPrize:
               doors[p] = opened
               opened_doors += 1
   
       won_without = 0
       won_switch = 0
       if doors[player_pick] == picked_prize:
           won_without = 1
       while True:
           p = randint(0,bigN)
           if doors[p] != opened and  p != player_pick :
               if doors[p] == notPicked_prize:
                   won_switch = 1
               break
       return [won_without, won_switch]
       #run simulation for  10000000
       def main():
       overrall = [0,0]
       for bigN in range(0, 10000000):
           results = game()
           overrall [0] += results[0]
           overrall[1] += results[1]
       print "win without " + str(overrall[0]) +" win switch "+ str(overrall[1])
       print float(overrall[0])/float(overrall[1])
   main