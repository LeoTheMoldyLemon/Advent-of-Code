from copy import *
f=open("input.txt", "rt")
a=f.readline()
l=[]
while a!="":
    a=a.split(",")
    for i in range(len(a)):
        a[i]=int(a[i])
    l.append(a)
    a=f.readline()


sides=[[0,0,1],[0,1,0],[1,0,0],[0,0,-1],[0,-1,0],[-1,0,0]]


def s(l1,l2):
    return [l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2]]

outside=[]

def checksides(cube):
    global l, outside
    res=0
    for i in sides:
        if s(i,cube) not in l:
            outside.append(s(i,cube))
            res+=1
    return res
res=0
for i in l:
    res+=checksides(i)

airp=[]

def adjecent(cube):
    global l
    res=[]
    for i in sides:
        if s(i,cube) not in l:
            res.append(s(i,cube))
    return res



def removedups(li):
    res=[]
    [res.append(x) for x in li if x not in res]
    return res

outside=removedups(outside)
def difference(l1, l2):
    res=[]
    [res.append(x) for x in l1 if x not in l2]
    return res

def checkpocket(cube):
    global l, outside
    passed=[]
    t=[cube]
    v=[]
    while t!=[]:
        nt=[]
        for i in t:
            
            if i==[0,0,0]:
                passed=removedups(passed)
                return [False, passed]
            for j in adjecent(i):
                if j not in v:
                    nt.append(j)
        nt=removedups(nt)
        v=deepcopy(t)
        passed.extend(t)
        t=deepcopy(nt)
    passed=removedups(passed)
    return [True, passed]

tocheck=deepcopy(outside)
while tocheck!=[]:
    print(tocheck)
    a=checkpocket(tocheck[0])
    tocheck=difference(tocheck, a[1])
    if not a[0]:
        outside=difference(outside,a[1])

def newchecksides(cube):
    global l, outside
    res=0
    for i in sides:
        if s(i,cube) not in outside and s(i,cube) not in l:
            res+=1
    return res

res=0
for i in l:
    res+=newchecksides(i)
print(res)



    
    

