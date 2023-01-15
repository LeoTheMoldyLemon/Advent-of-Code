test=False
if test:
    pos=[3,7]
else:
    pos=[3,9]



won=[0,0]

def thing(scr, pos, p, we):
    for i in range(3,10):
        nscr=list(scr)
        npos=list(pos)
        npos[p]=(npos[p]+i)%10
        nscr[p]+=npos[p]+1
        if i==6:
            nwe=we*7
        elif i in [5,7]:
            nwe=we*6
        elif i in [4,8]:
            nwe=we*3
        elif i in [3,9]:
            nwe=we*1
        
        if max(nscr)>=21:
            won[p]+=nwe
            if max(won)%10000000==0:
                print(won)
        else:
            thing(nscr, npos, (p+1)%2, nwe)



thing([0,0], pos, 0, 1)
print(won)









    
