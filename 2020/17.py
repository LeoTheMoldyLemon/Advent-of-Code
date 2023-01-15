f=f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
length=len(f.readlines())
print(length)
f.seek(0)
a=[]
for k in range(7):
    a.append([])
    for j in range(13):
        a[k].append([])
        for i in range(length+12):
            a[k][j].append("."*(length+12))
    


a.append([])
for j in range(6):
    a[7].append([])
    for i in range(length+12):
        a[7][j].append("."*(length+12))
    
a[7].append([])
for i in range(6):
    a[7][6].append("."*(length+12))
for i in range(length):
    x=f.readline()
    a[7][len(a[7])-1].append("."*6+x[0: len(x)-1]+"."*6)
for i in range(6):
    a[7][6].append("."*(length+12))

for j in range(6):
    a[7].append([])
    for i in range(length+12):
        a[7][7+j].append("."*(length+12))


for k in range(7):
    a.append([])
    for j in range(13):
        a[k+8].append([])
        for i in range(length+12):
            a[k+8][j].append("."*(length+12))


def broji(coords):
    global a


    adj=[-1,-1,-1,-1]
    result=0
    for i in range(81):
        if adj!=[0,0,0,0]:
            try:
                if a[coords[0]+adj[0]][coords[1]+adj[1]][coords[2]+adj[2]][coords[3]+adj[3]]=="#":
                    result+=1
            except IndexError:
                True
        adj[0]+=1
        if adj[0]==2:
            adj[0]=-1
            adj[1]+=1
        if adj[1]==2:
            adj[1]=-1
            adj[2]+=1
        if adj[2]==2:
            adj[2]=-1
            adj[3]+=1
    return result


for i in range(6):
    b=[]
    print(i)
    for j in range(len(a)):
        b.append([])
        for k in range(len(a[j])):
            b[j].append(a[j][k].copy()) 
    for w in range(len(a)):
        for z in range(len(a[w])):
            for y in range(len(a[w][z])):
                for x in range(len(a[w][z][y])):
                    count=broji([w,z,y,x])
                    try:
                        if count==3 and a[w][z][y][x]==".":
                            b[w][z][y]=b[w][z][y][:x]+"#"+b[w][z][y][x+1:]
                        if not (count==3 or count==2) and a[w][z][y][x]=="#":
                            b[w][z][y]=b[w][z][y][:x]+"."+b[w][z][y][x+1:]
                    except IndexError:
                        print(w,z,y,x)
                
    a=b.copy()
result=0
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            result+=a[i][j][k].count("#")
print(result)
    
    
                
                    
        
