f=open("input.txt", "r")
b=[]
a=f.readline()
while a!="":
    if a[len(a)-1]=="\n":
        a=a[:len(a)-1]
    b.append(a)
    a=f.readline()


z=[]
for i in range(len(b)):
    z.append("")
    for j in range(len(b[i])):
        z[i]+="o"
def check(x,y):
    checks=[False,False,False,False]
    try:
        if int(b[y][x])<=int(b[y][x-1]) and b[y][x]!="9":
            checks[0]=True
    except:
        checks[0]=True
    try:
        if int(b[y][x])<=int(b[y][x+1]) and b[y][x]!="9":
            checks[1]=True
    except:
        checks[1]=True
    try:
        if int(b[y][x])<=int(b[y-1][x]) and b[y][x]!="9":
            checks[2]=True
    except:
        checks[2]=True
    try:
        if int(b[y][x])<=int(b[y+1][x]) and b[y][x]!="9":
            checks[3]=True
    except:
        checks[3]=True
    return(checks[0] and checks[1] and checks[2] and checks[3])


def travel(x,y):
    if b[y][x]=="9":
        return "edge"
    if check(x,y):
        return [x,y]
    if x+1<len(b[0]):
        if int(b[y][x])>int(b[y][x+1]):
            return travel(x+1, y)
        
    if x>0:
        if int(b[y][x])>int(b[y][x-1]):
            return travel(x-1, y)
        
    if y+1<len(b):
        if int(b[y][x])>int(b[y+1][x]):
            return travel(x, y+1)
        
    if y>0:
        if int(b[y][x])>int(b[y-1][x]):
            return travel(x, y-1)

c1=[]
c2=[]
for i in range(len(z)):
    print(z[i])
for i in range(len(b)):
    for j in range(len(b[i])):
        k=travel(j,i)
        if k!="edge":
            if k in c1:
                c2[c1.index(k)]+=1
            else:
                c1.append(k)
                c2.append(1)
            z[i]=z[i][:j]+str(c1.index(k)%10)+z[i][(j+1):]
print(c2)

for i in range(len(z)):
    print(z[i])





