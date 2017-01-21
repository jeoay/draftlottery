# randomizes draft order based on designated percentages, exclude those already picked
import random

draft_num =  random.random()

teams = ['Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12', 'Turkaton', 'Team Hand Hugs']

team7 = 0.25
team8 = 0.43
team9 = 0.58
team10 = 0.71
team11 = 0.83
team12 = 0.93
team13 = 0.98
team14 = 1.0

def order():
    #need to loop through if statement to print each one and make those True if they already appeared. 
    print draft_num
    if draft_num <= team7 and team7 != True:
        print teams[0]
        team7 = True
    elif draft_num <= team8 and team8 != True:
        print teams[1]
        
    elif draft_num <= team9 and team9 != True:
        print teams[2]
        
    elif draft_num <= team10 and team10 != True:
        print teams[3]
        
    elif draft_num <= team11 and team11 != True:
        print teams[4]
        
    elif draft_num <= team12 and team12 != True:
        print teams[5]
        
    elif draft_num <= team13 and team13 != True:
        print teams[6]
        
    elif draft_num <= team14 and team14 != True:
        print teams[7]
        
    else:
        print "Something went wrong"

order()
