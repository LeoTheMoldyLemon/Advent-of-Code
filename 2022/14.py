import copy
f=open("input.txt", "rt")
a=f.readline()
l=[]
m=[]
while a!="":
    a=a.replace("\n", "").split(" -> ")
    l.append([])
    for i in range(len(a)):
        l[-1].append([])
        a[i]=a[i].split(",")
        for j in range(len(a[i])):
            l[-1][-1].append(int(a[i][j]))
    a=f.readline()
print(l)

ver=[1000,0]
hor=[1000,0]
start=[100, 500]
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j][1]>ver[1]:
            ver[1]=l[i][j][1]
            
        if l[i][j][1]<ver[0]:
            ver[0]=l[i][j][1]
            
        if l[i][j][0]>hor[1]:
            hor[1]=l[i][j][0]
            
        if l[i][j][0]<hor[0]:
            hor[0]=l[i][j][0]

start[1]-=hor[0]-426
hor[1]-=hor[0]

def printmap(m):
    for i in range(len(m)):
        s=""
        for j in range(len(m[i])):
            s+=m[i][j]
        print(s)



        
start[0]=0

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j][0]-=hor[0]-426
        
hor=hor[1]
ver=ver[1]
print(l)


for i in range(ver+1):
    m.append([])
    for j in range(hor+853):
        m[-1].append(".")
m.append([])
for i in range(hor+853):
    m[-1].append(".")
m.append([])
for i in range(hor+853):
    m[-1].append("#")


for i in l:
    m[i[0][1]][i[0][0]]="#"
    for j in range(1,len(i)):
        if(i[j][1]>i[j-1][1]):
            for k in range(i[j-1][1]+1, i[j][1]+1):
                m[k][i[j][0]]="#"
                
        elif(i[j][1]<i[j-1][1]):
            for k in range(i[j-1][1]-1, i[j][1]-1, -1):
                m[k][i[j][0]]="#"
                
        elif(i[j][0]>i[j-1][0]):
            for k in range(i[j-1][0]+1, i[j][0]+1):
                m[i[j][1]][k]="#"
                
        elif(i[j][0]<i[j-1][0]):
            for k in range(i[j-1][0]-1, i[j][0]-1, -1):
                m[i[j][1]][k]="#"


def move(coords):
    y=coords[0]
    x=coords[1]
    global m
    if(m[y+1][x]=="."):
        return [y+1, x]
    elif(m[y+1][x-1]=="."):
        return [y+1, x-1]
    elif(m[y+1][x+1]=="."):
        return [y+1, x+1]
    else:
        return [y, x]
    
    




res=0
while True:
    coords=copy.deepcopy(start)
    while True:
        ncoords=move(coords)
        if(m[start[0]][start[1]]=="o"):
            print(res)
            break
        if(ncoords==coords):
            m[coords[0]][coords[1]]="o"
            res+=1
            break
        coords=copy.deepcopy(ncoords)
        
















        
         
