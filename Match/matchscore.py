def printAll(players):
    print(f"SNo\tName\tInning\tRun\tWicket\tMatch")
    for player in players:
        print(f"{player[0]}\t{player[1]}\t{player[2]}\t{player[3]}\t{player[4]}\t{player[5]}")
players = [
   
    (1,"Roshan",10,100,6,4,1),
    (2,"Kishan",10,100,6,4,1),
    (3,"Amit",10,100,6,4,1),
    (4,"Champak",10,100,6,4,1)
]

print("Input")
printAll(players)
print("1-SNo,2-Name,3-Inning,4-Run,5-Wicket,6-Match")   
option=int(input())
players.sort(key=lambda players: players[option-1])
print("\nSorted")
printAll(players)