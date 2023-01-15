f=open("testinput.txt", "r")
a=[]
b=f.readline()
while b!="":
    a.append([])
    for i in range(len(b)):
        if b[i]!="\n":
            a[len(a)-1].append(int(b[i]))
    b=f.readline()
print(a)

m=[]
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[i].append(1)
result=0

def check(y,x):
    global result
    if a[y][x]<10:
        return False
    f[y][x]=1
    a[y][x]=0
    result+=1
    co=[-1,-1]
    for i in range(9):
        if co!=[0,0] and y+co[0]<len(a) and y+co[0]>-1 and x+co[1]<len(a[0]) and x+co[1]>-1:
            a[y+co[0]][x+co[1]]+=1
            check(y+co[0], x+co[1])
        co[0]+=1
        if co[0]==2:
            co[0]=-1
            co[1]+=1
    return True
i=0
while f!=m:
    i+=1
    f=[]
    for j in range(len(a)):
        f.append([])
        for k in range(len(a[j])):
            f[j].append(0)

    for y in range(len(a)):
        for x in range(len(a[y])):
            a[y][x]+=1
            check(y, x)
    for y in range(len(a)):
        for x in range(len(a[y])):
            if f[y][x]==1:
                a[y][x]=0
                
print(i)
