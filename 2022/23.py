from copy import *
f=open("inputf.txt", "rt")
a=f.readline()
m=[]
while a!="":
    a=a.replace("\n", "").replace(" ", "")
    m.append([])
    for i in a:
        m[-1].append(i)
    a=f.readline()

def printm():
    for i in m:
        s=""
        for j in i:
            s+=j
        print(s)


def printl():
    global l
    xmi=10000000
    xma=0
    ymi=10000000
    yma=0
    x=0
    y=0
    for i in l:
        if i[0]>xma:
            xma=i[0]
        if i[0]<xmi:
            xmi=i[0]
        if i[1]>yma:
            yma=i[1]
        if i[1]<ymi:
            ymi=i[1]
    
    for i in range(ymi, yma+1):
        s=""
        for j in range(xmi, xma+1):
            if [j,i] in l:
                s+="#"
            else:
                s+="."
        print(s)
    print((xma-xmi+1)*(yma-ymi+1)-len(l))




def extendm(n):
    global m
    le=len(m)+2
    for i in range(n):
        m.insert(0,[])
        for j in range(len(m[i+1])+2*n):
            m[0].append(".")
    for i in range(n, len(m)):
        for j in range(n):
            m[i].insert(0,".")
            m[i].append(".")
    for i in range(n):
        m.append([])
        for j in range(le+2*n):
            m[-1].append(".")
            
#extendm(8)
#printm()

l=[]
for i in range(len(m)):
    for j in range(len(m[i])):
        if "#"==m[i][j]:
            l.append([j,i])
print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
printl()
print("AAAAAAAAAAAAAAAAAAAAAAAAAA")

checks=[[[0,-1],[[-1,-1],[0,-1],[1,-1]]],[[0,1],[[-1,1],[0,1],[1,1]]],[[-1,0],[[-1,-1],[-1,0],[-1,1]]],[[1,0],[[1,-1],[1,0],[1,1]]]]
around=[[1,0], [1,1],[0,1],[-1,1],[-1,0], [-1,-1],[0,-1],[1,-1]]          

def getmoves():
    global l, checks, around
    moves=[]
  
    for i in range(len(l)):
        #print(l[i])
        empty=True
        for j in range(len(around)):
            if [l[i][0]+around[j][0],l[i][1]+around[j][1]] in l:
                empty=False
                break
        if empty:
            moves.append(l[i])

        if not empty:
            for j in range(len(checks)):
                good=True
                for k in range(len(checks[j][1])):
                    if [l[i][0]+checks[j][1][k][0],l[i][1]+checks[j][1][k][1]] in l:
                        good=False
                if good:
                    moves.append([l[i][0]+checks[j][0][0], l[i][1]+checks[j][0][1]])
                    break
            if not good:
                moves.append(l[i])
        #print(moves[i])
    return moves
f=0
while True:
    moves=getmoves()
    for j in range(len(moves)):
        for k in range(len(moves)):
            if k!=j and moves[k]==moves[j]:
                moves[k]=l[k]
                moves[j]=l[j]
    f+=1
    if l==moves:
        break
    l=deepcopy(moves)
    nchecks=checks[1:]
    nchecks.append(checks[0])
    checks=deepcopy(nchecks)
print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
printl()
print(f)
















