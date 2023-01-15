f=open(r"D:\desktop\Programming\Advent of code\2020\input.txt", "r")
a=["."*99]
length=len(f.readlines())
f.seek(0)
for i in range(length):
    a.append("."+f.readline().split("\n")[0]+".")
a.append("."*99)
def see(x, y, coords):
    try:
        if a[y+coords[0]][x+coords[1]]==".":
            if 99>y+2*coords[0]>-1 and 96>x+2*coords[1]>-1:
                return see(x+coords[1], y+coords[0], coords)
            else:
                return 0
        elif a[y+coords[0]][x+coords[1]]=="L":
            return 0
        else:
            return 1 
    except(IndexError):
        print("ERROR: x:"+str(x)+", y:"+str(y)+", cx:"+str(coords[1])+", cy:"+str(coords[0]))


while True:
    b=["."*99]
    for y in range(1, len(a)-1):
        b.append(".")
        for x in range(1, len(a[y])-1):
            if a[y][x]!=".":
                coords=[-1, -1]
                occ=0
                for j in range(9):
                    if coords!=[0,0]:
                        #occ+=see(x,y,coords)
                        if a[y+coords[0]][x+coords[1]]=="#":
                           occ+=1
                    coords[0]+=1
                    if coords[0]>1:
                        coords=[-1, coords[1]+1]
                if occ==0 and a[y][x]=="L":
                    b[y]+="#"
                elif occ>4 and a[y][x]=="#":
                    b[y]+="L"
                else:
                    b[y]+=a[y][x]
            else:
                b[y]+="."
        b[y]+="."
    b.append("."*99)
    if a==b:
        break
    a=b.copy()

        
    
br=0
for i in range(len(a)):
    br+=a[i].count("#")
print(br)
