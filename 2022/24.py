from copy import *
f=open("inputf.txt", "rt")
a=f.readline()
m=[]
while a!="":
    a=a.replace("\n", "")
    m.append([])
    for i in a:
        m[-1].append(i)
    a=f.readline()

def printm():
    for i in range(len(m)):
        s=""
        for j in range(len(m[i])):
            s+=m[i][j]
        print(s)

printm()

l=[]


dirs={(1,0):">",(-1,0):"<",(0,-1):"^",(0,1):"v",}

def printl():
    global l, dirs, m
    sm=[]
    for i in range(len(m)):
        s=""
        for j in range(len(m[i])):
            num=0
            last=()
            for k in l:
                if [j,i]==k[0]:
                    num+=1
                    last=k[1]
            if num>0:
                if num==1:
                    s+=dirs[last]
                else:
                    s+=str(num)
            elif m[i][j] in "<>^v":
                s+="."
            else:
                s+=m[i][j]
        sm.append(s)
    
    for i in sm:
        print(i)
        
        






for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==">":
            l.append([[j,i],(1,0)])
        elif m[i][j]=="<":
            l.append([[j,i],(-1,0)])
        elif m[i][j]=="v":
            l.append([[j,i],(0,1)])
        elif m[i][j]=="^":
            l.append([[j,i],(0,-1)])

print(l)


def movebliz(l):
    global m
    for i in l:
        if m[i[0][1]+i[1][1]][i[0][0]+i[1][0]]=="#":
            if i[1][0]==1:
                i[0][0]=1
            elif i[1][0]==-1:
                i[0][0]=len(m[0])-2
            elif i[1][1]==1:
                i[0][1]=1
            elif i[1][1]==-1:
                i[0][1]=len(m)-2
        else:
            i[0][1]+=i[1][1]
            i[0][0]+=i[1][0]
    return l


movs=[[0,1],[0,-1],[1,0],[-1,0],[0,0]]

def moves(pos, l, k):
    global m, movs
    move=[]
    for i in movs:
        if 0<=pos[1]+i[1]<len(m) and 0<=pos[0]+i[0]<len(m[0]):
            if m[pos[1]+i[1]][pos[0]+i[0]]!="#":
                empty=True
                for j in l:
                    if [pos[0]+i[0],pos[1]+i[1]]==j[0]:
                        empty=False
                if empty:
                    move.append([pos[0]+i[0],pos[1]+i[1], k])
    return move
            









ex=[len(m[0])-2, len(m)-1]
vis=[]
tov=[[1,0,0]]
k=0
res=0
done=False
while len(tov)!=0 and not done:
    k+=1
    res+=1
    k%=600
    ntov=[]
    nl=movebliz(l)
    for i in tov:
        for j in moves(i[:2], nl ,k):
            if j not in tov and j not in vis and j not in ntov:
                if j[:2]==ex:
                    print(res)
                    done=True
                ntov.append(j)
    l=deepcopy(nl)
    vis.extend(tov)
    tov=deepcopy(ntov)
    #print(tov)
    #printl()
    print(res)
print("end")


ex=[1,0]
vis=[]
tov=[[len(m[0])-2, len(m)-1,k]]
done=False
while len(tov)!=0 and not done:
    k+=1
    res+=1
    k%=600
    ntov=[]
    nl=movebliz(l)
    for i in tov:
        for j in moves(i[:2], nl ,k):
            if j not in tov and j not in vis and j not in ntov:
                if j[:2]==ex:
                    print(res)
                    done=True
                ntov.append(j)
    l=deepcopy(nl)
    vis.extend(tov)
    tov=deepcopy(ntov)
    #print(tov)
    #printl()
    print(res)
print("end")


ex=[len(m[0])-2, len(m)-1]
vis=[]
tov=[[1,0,k]]
done=False
while len(tov)!=0 and not done:
    k+=1
    res+=1
    k%=600
    ntov=[]
    nl=movebliz(l)
    for i in tov:
        for j in moves(i[:2], nl ,k):
            if j not in tov and j not in vis and j not in ntov:
                if j[:2]==ex:
                    print(res)
                    done=True
                ntov.append(j)
    l=deepcopy(nl)
    vis.extend(tov)
    tov=deepcopy(ntov)
    #print(tov)
    #printl()
    print(res)
print("end")
    

    



    















