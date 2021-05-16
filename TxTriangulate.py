
# TxTriangulate
# Twitter engine
# Written By ef1500
# Used to find the mutals between two accounts. This usually means that there is some sort of mutual
# Connection and that's exactly what I'm after here. 

import twitter
import numpy as np
import time

Ckey=''
Csc=''
Atk=''
Ats=''

#Ckey=''
#Csc=''
#Atk=''
#Ats=''

#Startup Twitter api
api = twitter.Api(consumer_key=Ckey,
                  consumer_secret=Csc,
                  access_token_key=Atk,
                  access_token_secret=Ats)

# +============Basic Definitions=========+
mx_count = 300  #Total number of followers to return



# Alright Let's do this
def GrabIDs(targetA, targetB):
    TaL = api.GetFriends(screen_name = targetA, total_count=mx_count)
    TbL = api.GetFriends(screen_name = targetB, total_count=mx_count)
    Usr1 = [u.screen_name for u in TaL]
    Usr2 = [v.screen_name for v in TbL]
    Mutuals = []
    L2x = []
    print("Target A's Friend List " + str(Usr1))
    print("Target B's Friend List " + str(Usr2))
    for element in Usr1:
        if element in Usr2:
            print("Found Root Mutual " + str(element))
            Mutuals.append(str(element))
    # The next thing that we need to implement is going through friend of friends. 
    # A quick rundown of the logic here
    # If Mutal: Assume(Associate) & appendTo(Mutuals) Basically, add them to the main list of search canidates that we are going to search for.
    # Assume all mutuals are connected directly to the target(s) in some way shape or form and then add them to the main list to be analyzed. 
    FX = open('Log.txt', 'w')
    for ux in Mutuals:
        try:
            uxl = api.GetFriends(screen_name=str(ux), total_count=mx_count)
            gxl = [k.screen_name for k in uxl]
        except twitter.error.TwitterError:
            print("Fuck you twitter API!")
            continue
        for User in gxl:
            if User in Usr1:
                print("Found Semi-Mutual " + str(User) + '\0' + "Semi-Mutual friend of " + str(ux))
                print("Found Semi-Mutual " + str(User) + '\0' + "Semi-Mutual friend of " + str(ux), file=FX)
                FX.close
                L2x.append(User)
            if User in Usr2:
                print("Found Semi-Mutual " + str(User) + '\0' + "Semi-Mutual friend of " + str(ux))
                print("Found Semi-Mutual " + str(User) + '\0' + "Semi-Mutual friend of " + str(ux), file=FX)
                FX.close
                L2x.append(User)
    #L2x is now full of Both targets' semi mutuals, we can forwar propagate the users to the next stage.
    #This next stage will be finding the mutuals of the semi-mutuals. 
    
    for uyer in L2x:
        try:
            Gnx = api.GetFriends(screen_name = str(uyer), total_count=mx_count)
            gyl = [m.screen_name for m in Gnx]
        except twitter.error.TwitterError:
            print("Fuck you, Twitter api!")
            continue
        for uxer in gyl:
            if uxer in Usr1:
                print("Found Layer 2 Root Mutual " + str(uxer) + '\0' + 'Mutual of ' + str(targetA))
                print("Found Layer 2 Root Mutual " + str(uxer) + '\0' + 'Mutual of ' + str(targetA), file=FX)
                Mutuals.append(str(uxer))
                FX.close
            if uxer in Usr2:
                print("Found Layer 2 Root Mutual " + str(uxer) + '\0' + 'Mutual of ' + str(targetB))
                print("Found Layer 2 Root Mutual " + str(uxer) + '\0' + 'Mutual of ' + str(targetB), file=FX)
                Mutuals.append(str(uxer))
                FX.close
#        except twitter.error.TwitterError:
#            print("Fuck you, Twitter api!")
#            print(str(Mutuals))
#            return Mutuals
    print(str(Mutuals))
    return Mutuals

def GrabMx(targetA, targetB):
    TaL = api.GetFriends(screen_name = targetA, total_count=mx_count)
    TbL = api.GetFriends(screen_name = targetB, total_count=mx_count)
    Usr1 = [u.screen_name for u in TaL]
    Usr2 = [v.screen_name for v in TbL]
    Mutuals = []
    L2x = []
    print("Target A's Friend List " + str(Usr1))
    print("Target B's Friend List " + str(Usr2))
    for element in Usr1:
        if element in Usr2:
            print("Found Root Mutual " + str(element))
            Mutuals.append(str(element))
    return Mutuals
