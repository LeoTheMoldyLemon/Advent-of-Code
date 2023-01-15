from copy import *
f=open("inputf.txt", "rt")
ss=50
a=f.readline()
m=[]
l=[]
while a!="\n":
    m.append(a.replace("\n", ""))
    a=f.readline()
l=f.readline().replace("\n", "")

nl=[]
nex=""
print(l)
for i in range(len(l)):
    if nex!="" and l[i] in "RL":
        nl.append(int(nex))
        nex=""
    if l[i] in "RL":
        nl.append(l[i])
    else:
        nex+=l[i]
if nex!="":
    nl.append(int(nex))
l=copy(nl)
print(l)

def printc(x,y,d):
    global m,dirs
    for i in range(len(m)):
        s=""
        for j in range(len(m[i])):
            if i==y and j==x:
                s+=">v<Ʌ"[dirs.index(d)]
            else:
                s+=m[i][j]
        
        print(s)


def testcubewalk(mov):
    global l, ss, m
    tests=[[2*ss+mov, 1, [-1, 0]],[mov, ss+1, [-1, 0]], [ss+mov, ss+1, [-1, 0]], [3*ss+mov, 2*ss+1, [-1,0]], [mov, 2*ss, [1,0]], [ss+mov, 2*ss, [1,0]], [2*ss+mov, 3*ss, [1,0]], [3*ss+mov, 3*ss, [1,0]],[3*ss, mov, [0,1]],[3*ss, ss+mov, [0,1]],[4*ss, 2*ss+mov, [0,1]],[2*ss+1, mov, [0,-1]],[1, ss+mov, [0,-1]],[2*ss+1,2*ss+mov , [0,-1]]]
    for i in range(len(tests)):
        printc(tests[i][0], tests[i][1], tests[i][2])
        a=cubewalk(tests[i][0], tests[i][1], tests[i][2])
        printc(a[0], a[1], a[2])
        

def cubewalk(x,y,d):
    global dirs, m, ss
    if d==[-1,0]:
        if y==1:
            nd=[1,0]
            ny=1+ss
            nx=3*ss-x+1
        elif y==1+ss:
            if x<=ss:
                nd=[1,0]
                ny=1
                nx=3*ss-x+1
            else:
                nd=[0,1]
                ny=x-ss
                nx=2*ss+1
        else:
            nd=[0,-1]
            nx=3*ss
            ny=5*ss-x+1
    elif d==[1, 0]:
        if y==2*ss:
            if x<=ss:
                nd=[-1,0]
                ny=3*ss
                nx=3*ss-x+1
            else:
                nd=[0,1]
                nx=2*ss+1
                ny=4*ss-x+1
        else:
            if x<=3*ss:
                nd=[-1,0]
                ny=2*ss
                nx=3*ss-x+1
            else:
                nd=[0,1]
                nx=1
                ny=5*ss-x+1
    elif d==[0,1]:
        if x==3*ss:
            if y<=ss:
                nd=[0,-1]
                nx=4*ss
                ny=3*ss-y+1
            else:
                nd=[1,0]
                ny=2*ss+1
                nx=5*ss-y+1
        else:
            nd=[0,-1]
            nx=3*ss
            ny=3*ss-y+1
    elif d==[0,-1]:
        if x==1:
            nd=[-1,0]
            ny=3*ss
            nx=5*ss-y+1
        else:
            if y<=ss:
                nd=[1,0]
                ny=ss+1
                nx=ss+y
            else:
                nd=[-1, 0]
                ny=2*ss
                nx=4*ss-y+1
    return [nx,ny,nd]





def printm():
    global m,x,y,d, dirs
    for i in range(len(m)):
        s=""
        for j in range(len(m[i])):
            if i==y and j==x:
                s+=">v<Ʌ"[dirs.index(d)]
            else:
                s+=m[i][j]
        
        print(s)


dirs=[[0, 1], [1, 0], [0, -1], [-1, 0]]

ma=0
for i in range(len(m)):
    if len(m[i])>ma:
        ma=len(m[i])
ma+=1
for i in range(len(m)):
    m[i]=m[i]+" "*(ma-len(m[i]))

m.insert(0, " "*ma)
m.append(" "*ma)
for i in range(len(m)):
    m[i]=" "+m[i]




def step(x,y,d):
    global m, dirs
    ny=y+d[0]
    nx=x+d[1]
    nd=d
    walk=False
    if m[ny][nx]==" ":
        a=cubewalk(x,y,d)
        nx=a[0]
        ny=a[1]
        nd=a[2]
        print("walkin")
        walk=True
        #printm()
    if m[ny][nx]=="#":
        return [x,y,d,True, False, walk]
    elif m[ny][nx]==" ":
        print("error ")
        print(nx,ny,nd)
        return [x,y,d,True,True, walk]
    else:
        return [nx, ny, nd,False,False, walk]

x=0
y=0
d=dirs[0]
found=False
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]!=" ":
            x=j
            y=i
            found=True
            break
        
    if found:
        break


for i in range(len(l)):
    #print(l[i], i, len(l))
    if isinstance(l[i],str):
        if l[i]=="R":
            d=dirs[(dirs.index(d)+1)%len(dirs)]
        else:
            d=dirs[(dirs.index(d)-1)%len(dirs)]
        #printm()
    else:
        for j in range(l[i]):
            a=step(x,y,d)
            if a[4]:
                print(x,y,d)
                printm()
            x=a[0]
            y=a[1]
            d=a[2]
            if a[5]:
                print(i, j)
                #printm()
            if a[4]:
                print(x,y,d)
                printm()
            if a[3]:
                break
            #printm()

print(y,x,dirs.index(d), 1000*y+4*x+dirs.index(d))
