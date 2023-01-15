f=open(r"input.txt", "r")
x=f.readline()
deck=[[],[]]
for i in range(2):
    x=f.readline()
    while x!="\n" and x!="" and x!="Player 2:\n":
        deck[i].append(int(x[:len(x)-1]))
        x=f.readline()

def combat(deck):
    repeat=[]
    print("new game")
    win=-1
    while len(deck[0])!=0 and len(deck[1])!=0:
        repeat.append([deck[0].copy(), deck[1].copy()])
        draw=[deck[0][0], deck[1][0]]
        del(deck[0][0])
        del(deck[1][0])
        if draw[0]>len(deck[0]) or draw[1]>len(deck[1]):
            if draw[0]>draw[1]:
                draw=reversed(sorted(draw))
                deck[0].extend(draw)
            else:
                draw=reversed(sorted(draw))
                deck[1].extend(draw)
        else:
            winner=combat([deck[0][0:(draw[0])], deck[1][0:(draw[1])]])[0]
            deck[winner].append(draw[winner])
            if winner==0:
                deck[winner].append(draw[1])
            else:
                deck[winner].append(draw[0])
        if deck in repeat:
            win=0
            deck=deck[0].copy()
            break
    if win==-1:
        if len(deck[0])!=0:
            win=0
            deck=deck[0].copy()
        else:
            win=1
            deck=deck[1].copy()
    score=0
    for i in range(len(deck)):
        score+=deck[i]*(len(deck)-i)
    return(win, score)
print(combat(deck))                                                                     
        
