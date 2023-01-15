m=[]
for i in range(323):
    m.append(input())
w=len(m[0])
l=len(m)
def collision(w, l, hm, vm, m):
    coords=[0,0]
    b=0
    while coords[1]<l:
        print(coords)
        if m[coords[1]][coords[0]]=="#":
            b+=1
        coords[0]+=hm
        coords[1]+=vm
        if coords[0]>=w:
            coords[0]-=w
    return(b)
f=collision(w, l, 1, 1, m)
g=collision(w, l, 3, 1, m)
h=collision(w, l, 5, 1, m)
j=collision(w, l, 7, 1, m)
k=collision(w, l, 1, 2, m)
print(f,g,h,j,k)
print(f*g*h*j*k)
