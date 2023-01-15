from time import *
tim=time()
f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
x=f.readline()
rules=[]
while x!="\n":
    rules.append([x.split(":")[0],
                 [[int(x.split(":")[1].split(" or ")[0][1:].split("-")[0]),
                   int(x.split(":")[1].split(" or ")[0].split("-")[1])],
                  [int(x.split(":")[1].split(" or ")[1].split("-")[0]),
                   int(x.split(":")[1].split(" or ")[1][:len(x.split(":")[1].split(" or ")[1])-1].split("-")[1])]]
                 ])
    x=f.readline()

x=f.readline()
x=f.readline()
myt=x.split(",")
for i in range(len(myt)):
    myt[i]=int(myt[i])
x=f.readline()
x=f.readline()
x=f.readline()
tic=[]
while x!="":
    tic.append(x.split(","))
    for i in range(len(tic[len(tic)-1])):
        tic[len(tic)-1][i]=int(tic[len(tic)-1][i])
    x=f.readline()
result=0
dellist=[]
for i in range(len(tic)):
    for j in range(len(tic[i])):
        check=False
        for k in range(len(rules)):
            if tic[i][j]>=rules[k][1][0][0] and tic[i][j]<=rules[k][1][0][1] or tic[i][j]>=rules[k][1][1][0] and tic[i][j]<=rules[k][1][1][1]:
                check=True
        if not check:
            dellist.append(tic[i])
for i in range(len(dellist)):
    tic.remove(dellist[i])
poss=[]
for i in range(len(myt)):
    poss.append([])
result=[]
for i in range(len(myt)):
    result.append([])
    for j in range(len(rules)):
        result[i].append(rules[j][0])
mid=[]
for i in range(len(myt)):
    mid.append([])
for i in range(len(tic)):
    for j in range(len(tic[i])):
        for k in range(len(rules)):
            if tic[i][j]>=rules[k][1][0][0] and tic[i][j]<=rules[k][1][0][1] or tic[i][j]>=rules[k][1][1][0] and tic[i][j]<=rules[k][1][1][1]:
                poss[j].append(rules[k][0])
    mid=result.copy()
    result=[]
    for i in range(len(poss)):
        result.append([])
        for j in range(len(poss[i])):
            if poss[i][j] in mid[i] and not poss[i][j] in result[i]:
                result[i].append(poss[i][j])
    poss=[]
    for j in range(len(myt)):
        poss.append([])
finresult=[]
for i in range(len(myt)):
    finresult.append("")
while "" in finresult:
    for i in range(len(result)):
        if len(result[i])==1:
            t=i
    finresult[t]=result[t][0]
    target=result[t][0]
    for i in range(len(result)):
        try:
            result[i].remove(target)
        except(ValueError):
            alah=0
result=1
n=0
for i in range(len(finresult)):
    if finresult[i][0:3]=="dep":
        result*=myt[i]
        n+=1
print(result, time()-tim)
