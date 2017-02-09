# randomizes draft order based on designated percentages, exclude those already picked

teams = ['Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12', 'Turkaton', 'Team Hand Hugs']


team7 = 0.25
team8 = 0.18
team9 = 0.15
team10 = 0.13
team11 = 0.12
team12 = 0.10
team13 = 0.05
team14 = 0.02

#print(teams)

def order():
    for t in teams:
        print t
        
if __name__ == "__main__":
    main()