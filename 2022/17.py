f=open("input.txt", "rt")
jets=f.readline()
jets.replace("\n", "")
rocks=[[[0,0],[0,1],[0,2],[0,3]],[[1,0],[0,1],[1,1],[2,1],[1,2]],[[0,0],[0,1],[0,2],[1,2],[2,2]],[[0,0],[1,0],[2,0],[3,0]],[[0,0],[1,0],[0,1],[1,1]]]
rocksh=[1,3,3,4,2]
rock=0
jet=0
m=[]

def ma(p):
    global m
    return m[p[0]][p[1]]

def s(p1, p2):
    return [p1[0]+p2[0], p1[1]+p2[1]]



def checkoverlap(r, pos):
    global rocks, m
    for i in rocks[r]:
        p=s(i,pos)
        if p[1]<0 or p[1]>6 or p[0]<0:
            return True
        if ma(p)=="#":
            return True
    return False

def printm():
    global m
    for i in range(len(m)-1, -1, -1):
        p=""
        for j in range(len(m[i])):
            p+=m[i][j]
        print(p)

def printmr(r,pos):
    global m, rocks
    for i in range(len(m)-1, -1, -1):
        p=""
        for j in range(len(m[i])):
            con=False
            for k in rocks[r]:
                if s(k, pos)==[i,j]:
                    p+="%"
                    con=True
            if not con:
                p+=m[i][j]
        print(p)
    print("")







def solidify(r, pos):
    global rocks, m
    for i in rocks[r]:
        a=s(pos, i)
        m[a[0]][a[1]]="#"



def extendm(h):
    global m
    for i in range(h-len(m)):
        m.append([])
        for j in range(7):
            m[-1].append(".")
extendm(7)
height=0
i=0
while True:
    pos=[height+3, 2]
    if rock==0:
        print(jet)
        if jet==0 or jet==33:
            
            print(height)
            print(i)
    if i==1440:
        print("I HERE")
        print(height)
    i+=1
    i%=1720
    while True:
        if jets[jet]==">":
            direc=[0,1]
        else:
            direc=[0,-1]

        if not checkoverlap(rock,s(pos, direc)):
            pos=s(pos, direc)

        jet+=1
        jet%=len(jets)
        
        if not checkoverlap(rock,s(pos, [-1,0])):
            pos=s(pos, [-1,0])
        else:
            height=max(height, pos[0]+rocksh[rock])
            solidify(rock,pos)
            extendm(height+7)
            break
        
        
    
    rock+=1
    rock%=len(rocks)
    
            

    
    
