f=open("input.txt", "rt")
a=f.readline()
l=[]
while a!="":
    l.append(a.replace("\n", ""))
    a=f.readline()
m=0

def calc(x,y):
    global l, m
    score=1
    h=0
    for i in range(x-1,-1,-1):
        h+=1
        if int(l[i][y])>=int(l[x][y]):
            break
    score*=h
    h=0
    for i in range(x+1,len(l)):
        h+=1
        if int(l[i][y])>=int(l[x][y]):
            break
    score*=h
    h=0
    for i in range(y-1,-1,-1):
        h+=1
        if int(l[x][i])>=int(l[x][y]):
            break
    score*=h
    h=0
    for i in range(y+1,len(l[x])):
        h+=1
        if int(l[x][i])>=int(l[x][y]):
            break
    score*=h
    return score
    







for i in range(len(l)):
    for j in range(len(l[i])):
        ah=calc(i,j)
        if ah>m:
            m=ah





