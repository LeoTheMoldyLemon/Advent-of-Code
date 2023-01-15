f=open("input.txt", "rt")
a=f.readline()
l=""
while a!="":
    a=a.replace("\n", "").split()
    a[1]=int(a[1])
    l+=a[0]*a[1]
    a=f.readline()

k=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
moves={"R":[1,0],"L":[-1,0],"U":[0,1],"D":[0,-1]}
pos=[]

def move(h, t):
    if abs(h[0]-t[0])>1 or abs(h[1]-t[1])>1:
        if h[0]!=t[0]:
            t[0]+=(h[0]-t[0])/abs(h[0]-t[0])
        if h[1]!=t[1]:
            t[1]+=(h[1]-t[1])/abs(h[1]-t[1])
    return t


for i in range(len(l)):
    k[0][0]+=moves[l[i]][0]
    k[0][1]+=moves[l[i]][1]

    for i in range(1, len(k)):
        k[i]=move(k[i-1], k[i])

    
    if k[9].copy() not in pos:
        pos.append(k[9].copy())

print(len(pos))

